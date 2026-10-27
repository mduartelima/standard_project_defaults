# Testes

Um diretório por camada, espelhando `src/`. Os testes do RAG ficam em `tests/rag/` (`python -m unittest discover -s tests/rag -v`).

| Camada | Pasta | Convenção |
|---|---|---|
| Backend | `tests/backend/` | unitários nos serviços, integração nas rotas |
| Frontend | `tests/frontend/` | componentes e hooks; estados de carregamento, erro e vazio |
| Firmware | `tests/firmware/` | lógica pura no host com HAL/BSP simulado; alvo real em `hil/` |
| Hardware | `tests/hardware/` | ERC/DRC, consistência pinout × esquemático × BSP, checklist de bring-up |
| RAG | `tests/rag/` | filtro por tipo, índice ausente, avaliação vazia |

Regras: bug corrigido ganha teste de regressão; resultados relevantes vão para `.ai/results/`.

Cada camada documenta no próprio README o comando de execução (`src/<camada>/README.md`).
