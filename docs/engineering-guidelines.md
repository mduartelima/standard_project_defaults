# Diretrizes de Engenharia e Desenvolvimento

## Gerais (todas as camadas)

- Mudança mínima e coesa; um objetivo por PR/commit.
- Todo erro tratado ou propagado explicitamente; nunca silenciado.
- Configuração por ambiente (`.env`, `sdkconfig`, `Kconfig`), nunca hardcoded. Segredos fora do git.
- Testes acompanham o código. Bug corrigido ganha teste de regressão.
- Interfaces entre camadas documentadas em `docs/architecture.md`.

## Backend

- Camadas: rotas/controladores → serviços (regra de negócio) → repositórios (dados).
- Validação de entrada na borda (schemas). Respostas de erro padronizadas.
- Logs estruturados (JSON) com correlação de requisição.
- Migrações de banco versionadas; nunca alterar schema manualmente.
- Testes: unitários nos serviços, integração nas rotas.

## Frontend

- Componentes pequenos e sem efeitos colaterais; lógica de dados em hooks/serviços.
- Estados de carregamento, erro e vazio sempre tratados.
- Acessibilidade: semântica HTML, rótulos, contraste, navegação por teclado.
- Tipagem estrita (TypeScript `strict`).

## Firmware

- **ISRs**: curtas, sem alocação, sem bloqueio, sem printf; sinalizar task via fila/flag/notificação.
- `volatile` e seções críticas para dados compartilhados com ISR ou entre tasks.
- Sem alocação dinâmica após inicialização (ou pools estáticos).
- Todo I/O com timeout; watchdog habilitado em produção.
- Camada HAL/BSP isolando acesso a hardware → lógica testável no host.
- Medir e registrar uso de Flash/RAM/stack a cada release (`.ai/results/`).
- Constantes de hardware (pinos, endereços I2C, clocks) centralizadas em um único header de BSP.
- Toda informação de registrador citada com a seção do datasheet/reference manual.

## Hardware

- Fonte de verdade: arquivos do EDA em `src/hardware/` (ex.: KiCad), versionados.
- `src/hardware/pinout.md` sincronizado com o esquemático e com o header de BSP do firmware.
- Revisão de esquemático: alimentação, desacoplamento, proteção ESD, pull-ups, níveis lógicos, pontos de teste.
- Cada revisão de placa registrada em `history.md` (Escopo: hardware) e em `decisions.md` se houver mudança de componente principal.

## Uso de IA no desenvolvimento

| Fazer | Evitar |
|---|---|
| Pedir plano antes de mudanças grandes | Aceitar diffs grandes sem revisão |
| Fornecer datasheet/trecho de código relevante | Deixar o modelo "lembrar" registradores e pinos |
| Exigir citação de fonte | Confiar em APIs não verificadas |
| Validar com build/testes/hardware real | Considerar "compila" como "funciona" |
| Registrar decisões e resultados | Deixar conhecimento apenas no chat |
