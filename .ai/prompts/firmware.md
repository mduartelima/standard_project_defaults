<alvo>
MCU/SoC: {{ex.: STM32G474, ESP32-S3, nRF52840}}
Framework/RTOS: {{ex.: ESP-IDF 5.x, Zephyr, FreeRTOS, bare-metal}}
Toolchain: {{ex.: arm-none-eabi-gcc 13}}
Recursos: Flash {{}} KB, RAM {{}} KB, clock {{}} MHz
</alvo>

<hardware>
Esquemático/pinout: `src/hardware/{{arquivo}}`
Periféricos envolvidos: {{UART2 @115200, I2C1 sensor 0x48, ...}}
</hardware>

<tarefa>
{{descrição}}
</tarefa>

<regras>
- Usar apenas registradores, pinos e APIs presentes no repositório ou no datasheet/manual indexado no RAG. Citar a seção do datasheet. Se a informação não estiver disponível, perguntar.
- ISR curta: sem alocação dinâmica, sem printf, sem bloqueio; sinalizar a task/loop principal.
- Todo I/O com timeout e código de erro tratado.
- `volatile` em variáveis compartilhadas com ISR; proteger seções críticas.
- Informar impacto estimado em Flash/RAM e reportar `size` do binário após build.
- Não gravar flash, fuses ou option bytes sem confirmação explícita.
</regras>

<validacao>
Build: `{{comando}}`. Teste em hardware: descrever procedimento e registrar em `.ai/results/`.
</validacao>
