# Análise — Referência de estrutura IoT industrial (monorepo)

**Data:** 2026-10-27  **Escopo:** geral

## Pergunta / problema

Avaliar se uma estrutura de monorepo para projetos IoT industriais (hardware, firmware com FOTA, protocolo, backend e frontend) enriquece ou polui o template.

## Fontes consultadas
- Texto de referência sem autoria nem citações, recebido do responsável (colado abaixo, sem emojis). Todas as afirmações técnicas dele são **não verificadas**.
- `docs/hardware-release.md`, `docs/ota-policy.md`, `docs/protocol.md`, `docs/architecture.md`.

## Fatos levantados

- O texto usa `hardware/`, `firmware/`, `backend/`, `frontend/` na raiz; o template usa `src/<camada>`.
- Versiona `hardware/electronics/manufacturing/` (Gerbers, BOM, pick-and-place); o template gera esses arquivos a partir da tag (`docs/hardware-release.md`).
- Fixa tecnologias: Protobuf, MCUboot, KiCad, Zephyr/FreeRTOS, Flutter/React Native, `imgtool`.
- Inclui escopo de produto IoT: Device Shadow, orquestrador de FOTA, séries temporais, app BLE/Wi-Fi.
- Contradição interna: guarda chaves em `ota-tools/` e as chama de "protegidas por CI/CD".
- Layout de slots "Slot 0, Slot 1 e Scratch" vale para alguns modos de swap do MCUboot; o modo DIRECT-XIP não tem rollback.

## Alternativas
| Opção | Prós | Contras | Esforço |
|---|---|---|---|
| Adotar a estrutura inteira | Cobre o ciclo completo | Reorganiza o template, fixa stack, pastas vazias | Alto |
| Ignorar | Nenhum custo | Perde 4 pontos úteis | Nenhum |
| Extrair 4 pontos (escolhida) | Ganho com baixo acoplamento | Exige manter o texto como referência | Baixo |

## Recomendação

Extrair: (1) padrões de chaves no `.gitignore` e regra de custódia em `SECURITY.md` e `docs/ota-policy.md`; (2) diretório de schemas do protocolo; (3) workflow de hardware desativado; (4) divisão opcional do firmware em `src/firmware/README.md`. Aplicado em 2026-10-27.

## Riscos e incertezas

- Afirmações do texto sem fonte primária; ler a documentação oficial do bootloader e do EDA antes de virar regra.
- O diretório de schemas não fixa Protobuf; a escolha fica por projeto.

## Texto de referência (original, sem emojis)

Uma estrutura padrão escalável para projetos IoT profissionais de nível industrial — abrangendo desde o design físico do produto até a nuvem, com suporte a múltiplos perfis de firmware e atualizações seguras — exige uma divisão clara baseada no ciclo de vida e na tecnologia de cada subsistema.
A arquitetura recomendada utiliza o conceito de Monorepo, organizada para isolar as responsabilidades de desenvolvimento (firmware, hardware, software) mantendo as interdependências fáceis de gerenciar.

Estrutura de Pastas Recomendada

```
meu-produto-iot/
├── .github/                   # CI/CD (Compilação automática de FW/SW, geração de Gerbers)
├── docs/                      # Arquitetura do sistema, manuais e diagramas de blocos
├── protocol/                  # Shared Schemas (Protobuf, JSON Schema para comunicação HW <-> Cloud)
│
├── hardware/                  # Engenharia Física
│   ├── electronics/           # Esquemas elétricos e layout da PCB (KiCad, Altium, Eagle)
│   └── mechanical/            # Gabinete, cases, moldes e suportes (STEP, STL, DXF)
│
├── firmware/                  # Engenharia de Embarcados
│   ├── bootloader/            # Código do MCUboot / Custom Bootloader
│   ├── targets/               # Aplicação principal separada por arquitetura/SO
│   │   ├── bare-metal/        # Aplicações sem SO de ultrabaixo consumo ou tempo real estrito
│   │   ├── rtos/              # Aplicações com FreeRTOS, Zephyr RTOS ou Azure RTOS
│   │   └── linux-embedded/    # Imagens Yocto/Buildroot ou scripts para Linux Embarcado
│   ├── ota-tools/             # Scripts de assinatura de imagem, criptografia e empacotamento FOTA
│   └── shared/                # Drivers e bibliotecas compartilhadas entre os targets
│
├── backend/                   # Infraestrutura Cloud / Servidor
│   ├── api/                   # REST / GraphQL / WebSockets para o Frontend
│   ├── iot-broker/            # Gateway MQTT / CoAP para recepção de telemetria e FOTA orchestrator
│   └── database/              # Migrações e modelagem (Time-series para telemetria + Relacional)
│
└── frontend/                  # Aplicações de Interface com o Usuário
    ├── web/                   # Dashboard administrativo e de usuários (React, Vue, etc.)
    └── mobile/                # App de provisionamento (BLE/Wi-Fi) e monitoramento (Flutter, RN)
```

Detalhamento dos Módulos Críticos


1. Hardware (/hardware)

Dividido estritamente para que engenheiros eletrônicos e mecânicos trabalhem sem conflitos.
• electronics/: Deve conter as pastas schematics/, pcb/ e manufacturing/ (arquivos Gerber, BOM com part numbers exatos da DigiKey/Mouser e arquivos Pick-and-Place para a montadora).
• mechanical/: Arquivos nativos de CAD e exportações em .step para validação de interferência mecânica (encaixe da PCB na carcaça).

2. Firmware, Segurança e FOTA (/firmware)

Desenhado para suportar o ciclo de vida completo do dispositivo e mitigar riscos de brick em atualizações.
• bootloader/: Configurações do MCUboot (árvore de chaves públicas/privadas, tabelas de partição de memória flash: Slot 0 (Active), Slot 1 (Secondary) e Scratch).
• targets/: Isola o código por complexidade. Projetos industriais complexos frequentemente usam um processador rodando Linux (Gateway) se comunicando com coprocessadores rodando RTOS ou Bare-metal (sensores/atuadores).
• ota-tools/: Armazena as chaves de assinatura (protegidas por CI/CD e nunca comitadas abertamente) e ferramentas como o imgtool do MCUboot para gerar os binários assinados e criptografados prontos para distribuição.

3. Protocolos de Comunicação (/protocol)

A "Single Source of Truth" (Fonte Única da Verdade) do projeto.
• Em vez de definir objetos JSON manualmente no firmware e no backend, utiliza-se buffers binários eficientes como Protocol Buffers (Protobuf) ou MessagePack.
• A partir de um único arquivo .proto, compila-se automaticamente o código de serialização/deserialização para C/C++ (firmware), TypeScript (frontend) e Go/Python/Node.js (backend).

4. Backend e Orquestração IoT (/backend)

O backend de um projeto IoT maduro geralmente é dividido em duas frentes:
• Ingestão de Dados (iot-broker): Serviços de alta performance dedicados a processar mensagens de milhares de dispositivos via MQTT/CoAP. É este módulo que gerencia o estado do dispositivo (Device Shadow) e envia os blocos do binário FOTA em pedaços (chunks) via pacotes controlados para o hardware.
• Regra de Negócio (api): Focada em autenticação, faturamento e entrega de dados estruturados para o Frontend.

Fluxo de Trabalho no CI/CD (Integração Contínua)

Com essa estrutura, um único Commit ou Pull Request pode acionar pipelines automatizados em paralelo:
1. Firmware Pipeline: Compila o código para os alvos (Zephyr/Linux), roda testes unitários nativos com mocks de hardware, assina o binário gerado usando o imgtool e faz o upload do artefato .bin ou .hex seguro para um bucket de homologação.
2. Software Pipeline: Roda linters e testes na API e no Frontend, gerando imagens Docker prontas para deploy em staging.
3. Hardware Pipeline: Roda scripts (como ferramentas CLI do KiCad) para validar regras de design elétrico (DRC) e exportar PDFs atualizados dos esquemáticos para documentação.

