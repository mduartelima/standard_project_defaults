# Release de hardware

## Versionamento

- Tag: `hw-<placa>-rev<X>` (ex.: `hw-<placa>-revA`).
- Revisão em letra após a liberação para fabricação; numeração antes disso, se o projeto adotar.
- Fontes (esquemático, layout) versionadas em `src/hardware/`. Saídas geradas **a partir da tag** e anexadas à release.

## Fluxo

1. Ramo a partir da última release; revisão por diff.
2. Merge e tag.
3. Silkscreen atualizado com a revisão antes de gerar os arquivos.
4. Geração de Gerbers, BOM e pick-and-place a partir da tag.
5. Anexar o pacote à release do repositório.
6. Registrar em `history.md` (Escopo: hardware) e, se houver troca de componente principal, em `decisions.md`.

## Checklist

- [ ] ERC sem erros
- [ ] DRC sem erros
- [ ] BOM conferida
- [ ] `src/hardware/pinout.md` × esquemático × header de BSP
- [ ] Silkscreen com a revisão correta
- [ ] Pacote de fabricação gerado a partir da tag
