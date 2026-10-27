# Plano: revisão, melhoria e validação do template fullstack + firmware + hardware

## Context

`ai-project-template/` é a estrutura-base para novos projetos e para atualizar projetos existentes. Os placeholders são intencionais e a revisão não os preenche com dados inventados. O pedido foi levantar os modelos de estrutura fullstack + firmware + hardware usados hoje e usá-los para revisar, melhorar e validar o template.

Decisões do usuário: o template segue **agnóstico** quanto a stack de firmware e EDA. A entrega é este plano. Na revisão do plano, o usuário pediu pesquisa dirigida de HIL, OTA/MCUboot e versionamento de hardware, e padrões para as lacunas. Também mudou a regra de `Co-Authored-By` (seção 4).

Nível de confiança das fontes: em maior parte blogs, fóruns e guias de fornecedores. Só a GitHub Docs e o ETSI são fontes primárias. Afirmações sem fonte primária estão marcadas como **não verificado**.

## 1. Modelos de referência atuais

| Área | Padrão recorrente | Aplicação agnóstica |
|---|---|---|
| Monorepo | Uma pasta por camada, CI por caminho | Manter `src/*`, adicionar CI por camada |
| Firmware (Zephyr) | Repositório da aplicação como manifesto `west.yml`, dependências fixadas por commit, testes no host com `native_sim` e Twister ([west](https://embeddedrelated.com/showarticle/1505.php), [guia Zephyr](https://hubble.com/community/guides/how-to-build-production-ready-iot-devices-with-zephyr-project-structure-debugging-and-field-deployment-patterns/)) | Exigir toolchain e dependências fixadas, seja qual for a ferramenta |
| Firmware (ESP-IDF/PlatformIO) | `main/` mais `components/`, testes Unity no host ([template ESP-IDF](https://awesome.ecosyste.ms/projects/github.com%2Fsivakov512%2Fesp-idf-project-template), [PlatformIO](https://docs.platformio.org/en/stable/frameworks/zephyr.html)) | Separar lógica pura do HAL/BSP |
| Testes | Unity/Ceedling no host com HAL mockado ([Ceedling](https://dev.to/einfochips/unit-testing-in-zephyr-rtos-projects-with-ceedling-a-developers-guide-1o6f)) | `tests/firmware/` host-first |
| CI embarcado | Container com toolchain fixada ([CI/CD embarcado](https://hubble.com/community/guides/how-to-set-up-ci-cd-for-embedded-projects/)) | Dockerfile ou devcontainer de build |
| Hardware (KiCad) | KiBot via YAML gera ERC/DRC, BOM, Gerbers e 3D no CI ([KiBot](https://kibot.readthedocs.io/en/master/introduction.html)) | Pasta de revisão e checklist, sem fixar o EDA |
| Agentes de IA | `AGENTS.md` mais MCP de PlatformIO/Zephyr ([Codex embarcado](https://codex.danielvaughan.com/2026/05/22/codex-cli-embedded-firmware-development-platformio-zephyr-mcp-agents-md-workflows/)) | Já coberto |

## 2. Pesquisa dirigida (comentário 1)

**HIL (hardware-in-the-loop)**
- Separar em dois estágios: build em runner de nuvem, flash e teste em runner self-hosted (por exemplo Raspberry Pi) roteado por label, como `has_esp32s3` ([Golioth](https://blog.golioth.io/?p=2789), [Golioth + pytest](https://blog.golioth.io/?p=6721)).
- Twister aceita um *hardware map* para limitar testes aos dispositivos listados. `--persistent-hardware-map` só funciona em Linux ([Twister](https://docs.zephyrproject.org/latest/develop/test/twister.html)).
- Critério de aprovação: o job só fica verde se build, flash, boot, estímulo e asserções passaram. Abrir a porta serial não conta. Rodar testes de host antes de ocupar a bancada ([guia](https://industrialmonitordirect.com/blogs/knowledgebase/configuring-github-actions-for-embedded-hil-testing)).
- Lacuna: não há referência única que combine pytest, Twister e hardware map num runner.
- **Sugestão para o template**: `tests/firmware/hil/README.md` com checklist da bancada (labels, mapa de dispositivos, critério de aprovação, fixture serial). Workflow HIL desativado por padrão.

**OTA / MCUboot**
- Modelo de duas slots (primária, secundária) com área de scratch. A aplicação confirma a imagem após autotestes (`boot_write_img_confirmed()`). Sem confirmação, o próximo reboot reverte ([Hubble](https://hubble.com/community/guides/zephyr-dfu-and-mcuboot-over-the-air-updates-with-rollback-protection/)).
- Falhas comuns vêm de geometria de slots, layout do trailer ou metadados de assinatura. Testar os caminhos pending, test, confirm, revert e upgrade permanente ([guia de integração](https://claudepluginhub.com/skills/easyzoom-aix-skills/mcuboot-integration)).
- O modo DIRECT-XIP não tem rollback e carrega a imagem de maior versão ([NXP](https://docs.mcuxpresso.nxp.com/mcuxsdk/latest/html/examples/ota_examples/_doc/flash_remap_readme.html)).
- A imagem precisa casar com o layout de partições e ser assinada com chave própria ([Nordic](https://devzone.nordicsemi.com/f/nordic-q-a/80502/option-to-roll-back-from-confirmed-image-slot-in-rare-ota-situations/333414)).
- Não foi alcançada a documentação oficial do MCUboot (docs.mcuboot.com). Consultar antes de virar regra.
- **Sugestão**: `docs/ota-policy.md` com campos a preencher: modo de swap, política de versão, assinatura, rollback, matriz de testes dos 5 caminhos, plano de rotação de chaves.

**Versionamento de hardware**
- Letra de revisão é o padrão da indústria, às vezes com número ([Altium](https://resources.altium.com/p/git-tagging-and-git-hardware-development-altium-designer)). SemVer é usado por alguns, mas contestado ([AllSpice](https://www.allspice.io/post/the-dangerous-art-of-versioning-in-hardware-design)). Híbrido comum: números antes do RTM, letras depois.
- Fluxo: ramo a partir do release, revisão por diff, merge, tag, geração dos arquivos de fabricação **a partir da tag**, silkscreen atualizado antes ([Zbotic](https://zbotic.in/pcb-version-control-manage-design-revisions/)).
- Fontes (esquemático, layout) são versionadas. Saídas (Gerbers, BOM, pick-and-place) são geradas no release e anexadas à tag ([Flux](https://www.flux.ai/p/blog/git-for-hardware)). Anexar o zip de Gerbers a um GitHub Release liga revisão, commit e arquivos de fabricação.
- **Sugestão**: convenção `hw-<placa>-rev<X>` para tags, `src/hardware/` com fontes e `releases/` fora do git (anexos de release), e checklist de release (ERC/DRC, BOM, pinout × esquemático, silkscreen).

## 3. Padrões e boas práticas para as lacunas (comentário 2)

| Lacuna | Existe padrão? | Recomendação |
|---|---|---|
| `SECURITY.md`, `CONTRIBUTING.md`, `SUPPORT.md`, `GOVERNANCE.md` | Sim, convenção documentada do GitHub ([community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)). O arquivo do repositório prevalece sobre o do repositório `.github` da organização | Incluir `SECURITY.md` e `CONTRIBUTING.md` no template. `SUPPORT.md` e `GOVERNANCE.md` opcionais |
| `CODEOWNERS`, `CHANGELOG` (Keep a Changelog) | Convenções conhecidas, mas **a pesquisa não retornou fonte**. Verificar na documentação oficial do GitHub e do Keep a Changelog | Incluir como stubs; confirmar sintaxe antes de gravar |
| Contratos firmware↔backend | Prática consolidada: evolução apenas aditiva (nunca mudar o comportamento existente, só acrescentar), Protobuf com campos novos e números reservados ([Cumulocity](https://community.cumulocity.com/t/cumulocity-iot-apis-sdks-and-compatibility/1449)), firmware MAJOR.MINOR.PATCH com bump de major para quebra ([Amazon ACK](https://developer.amazon.com/docs/ack/increment-device-firmware-version.html)). Registro de schemas para checar compatibilidade no CI (fontes de fornecedor, **não verificado**) | `docs/protocol.md` com regra aditiva, versão do contrato e checagem de compatibilidade no CI |
| Segurança de dispositivo | Sim: ETSI EN 303 645 (consumo; provisão 5.7 exige secure boot, alerta e limitação de função em caso de alteração não autorizada; avaliação por ETSI TS 103 701) ([resumo](https://www.smartsuite.com/frameworks/etsi-en-303-645-cyber-security-for-consumer-internet-of-things)). IEC 62443-4-2 e NIST IR 8259 aparecem só em material de fornecedores | `SECURITY.md` e `docs/ota-policy.md` referenciam ETSI EN 303 645. IEC 62443 e NIST IR 8259 ficam como **não verificado**: ler os textos primários antes de citar requisitos |
| Draft ETSI EN 304 623 (boot managers, ligado ao Cyber Resilience Act) | Rascunho (V0.1.3, 2026-06) | Só monitorar |
| Build, CI, ambiente (Docker, `.tool-versions`, `.editorconfig`, `.gitattributes`) | Prática comum, sem norma | Incluir como stubs genéricos |

## 4. Co-Authored-By (comentário 3)

Regra nova do usuário: **proibido de forma automática; permitido apenas se solicitado deliberadamente, a cada commit.**

- A atribuição padrão desta sessão manda incluir `Co-Authored-By: Claude...`. Pela regra do projeto e pelo comentário, **o agente não adiciona** a linha, salvo pedido explícito para aquele commit. Um pedido anterior não vale para o próximo.
- Isso muda a regra vigente (proibição absoluta) em `CLAUDE.md:27,52`, `docs/commit-convention.md:40,76`, `.gitmessage:9` e `.githooks/commit-msg:23,28`. Por `decisions.md`, a mudança exige **D-003** (append-only), com a regra anterior mantida no histórico.
- Aplicação sugerida: o agente nunca escreve o trailer por conta própria. O hook passa a aceitar o trailer apenas quando o commit é feito com `ALLOW_COAUTHOR=1` no ambiente, definido pelo usuário para aquele commit. Mantém o bloqueio de assinaturas "generated by" e de menções a IA.
- `settings.json`: manter `includeCoAuthoredBy: false` (ou `attribution` equivalente, após conferir a chave na documentação atual).
- **Ponto a confirmar**: o mecanismo `ALLOW_COAUTHOR=1` é uma proposta. Confirmar com o usuário antes de implementar.

## 5. Plano de melhoria (agnóstico, em ordem)

Um objetivo por commit, conforme `docs/commit-convention.md`.

1. **Decisão D-003** em `decisions.md`, depois ajuste de `CLAUDE.md`, `commit-convention.md`, `.gitmessage` e hook (seção 4).
2. **Corrigir inconsistências** (auditoria 2026-10-27)
   - `docs/api.md`, `docs/protocol.md`, `docs/datasheets/.gitkeep` e `.env.example` não existem: criar stubs ou remover as referências (`architecture.md:36-37`, `rag/README.md:17`, `.gitignore:7`).
   - `settings.json`: `python3`, `deny` ampliado (`git push -f`, `git reset --hard`, leitura de `.env`).
   - Hook: validar escopos de `.gitmessage:4`, testar em Git Bash no Windows.
   - RAG: `eval.py:21` (divisão por zero com `eval.json` vazio), `query.py:229-232` (filtro `--kind` após limitar a `k*5`), `query.py:222` (`sys.exit` dentro de `search()`). Indexar `.kicad_*`, BOM em CSV, `sdkconfig`. Peso maior para `datasheet`.
   - `.gitignore`: `*.bin`, `*.hex`, `*.elf`, `build/` ignorados globalmente podem esconder blobs legítimos.
3. **Governança e higiene**: `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`, `CHANGELOG.md`, `LICENSE` (escolha do usuário), `.editorconfig`, `.gitattributes` (LF em `.githooks/*`).
4. **READMEs por camada** (hoje 3 linhas idênticas): modelo com stack, build, teste, estrutura e dependências.
5. **Contratos e segurança**: `docs/protocol.md`, `docs/ota-policy.md` (seção 2).
6. **Hardware agnóstico**: convenção de tags e checklist de release (seção 2).
7. **CI e ambiente**: `.github/workflows/` por camada, desativados por padrão, devcontainer, `.tool-versions`, workflow HIL desativado.
8. **Testes**: `tests/{backend,frontend,firmware,hardware}/` com README de convenção, mais `tests/firmware/hil/README.md`.

Itens marcados **não verificado** (IEC 62443, NIST IR 8259, registro de schemas, CODEOWNERS, Keep a Changelog, docs oficiais do MCUboot) entram como campos a preencher até a leitura da fonte primária.

## 6. Validação

- Hook: executar `.githooks/commit-msg` com mensagens válidas e inválidas (formato, escopo, trailer com e sem `ALLOW_COAUTHOR=1`) em Git Bash no Windows, num repositório de teste (o diretório atual não é git).
- RAG: `python rag/ingest.py`, `python rag/eval.py` com `eval.json` preenchido e vazio, `query.py --kind` com resultados menores que `k`.
- Links: varrer o Markdown atrás de caminhos citados que não existem.
- `settings.json`: conferir a chave de atribuição com o agente `claude-code-guide`.
- Template aplicado: copiar para um diretório temporário vazio, `git init`, ativar o hook e fazer um commit de teste.
- Registrar em `.ai/results/` e numa entrada no topo de `ai-project-template/history.md`, em escrita impessoal.

## Arquivos críticos

- `ai-project-template/{CLAUDE.md,.gitmessage,.gitignore}`, `.githooks/commit-msg`, `.claude/settings.json`
- `ai-project-template/.ai/memory/decisions.md`, `docs/{commit-convention,architecture,engineering-guidelines}.md`
- `ai-project-template/rag/{config.json,ingest.py,query.py,eval.py,eval.json}`

## Fora de escopo

Fixar stack de firmware ou EDA, preencher placeholders com dados de um projeto real, e citar requisitos de IEC 62443 ou NIST IR 8259 sem ler os textos primários.
