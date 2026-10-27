# src/hardware — Hardware

> Modelo a preencher. Contexto geral: `docs/architecture.md`; regras: `docs/engineering-guidelines.md`; release: `docs/hardware-release.md`.

## Placa

| Item | Valor |
|---|---|
| Nome da placa | <nome> |
| Revisão atual | <ex.: revA> |
| MCU | <modelo> |
| Ferramenta EDA (versão fixada) | <ex.: KiCad X.Y> |

## Estrutura

```
<arquivos de esquemático, layout, bibliotecas de símbolos/footprints>
```

Fontes ficam versionadas aqui. Saídas de fabricação (Gerbers, BOM, pick-and-place) são geradas na release e anexadas à tag, não versionadas.

## Verificações

- ERC e DRC sem erros.
- `pinout.md` sincronizado com o esquemático e com o header de BSP do firmware.
