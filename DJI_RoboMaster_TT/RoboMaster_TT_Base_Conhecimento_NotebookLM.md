# DJI RoboMaster TT (Tello Talent) — Base de Conhecimento Mestre (CTE Informático)

> **Contexto do Documento (Fonte Única de Verdade · Web, Manuais e NotebookLM)**
> - **Instituição / Espaço:** Centro Tecnológico Especializado (CTE) Informático
> - **Equipamento:** Drone Educativo Programável **DJI RoboMaster TT (Tello Talent)**
> - **Código de Inventário CTE:** `INV-144` (**10 unidades** · Estúdio 4C · Armário `D1.4C-MF-A04`)
> - **Público-Alvo:** Alunos e professores de programação, robótica, matemática, física e projetos interdisciplinares.
> - **Regra de Utilização no CTE:** Uso **exclusivamente em interiores** bem iluminados (`3 × 3 m` livres) e com os **4 protetores de hélices sempre montados**.

---

## 1. Especificações Principais

| Característica | Valor Oficial (RoboMaster TT) |
| :--- | :--- |
| **Peso e Dimensões** | `87 g` (drone + hélices + protetores + bateria) + `~12,5 g` (módulo ESP32) · `98 × 92,5 × 41 mm` |
| **Módulo Open-Source** | **ESP32-D2WD** dual-core `160 MHz` · Suporte Arduino / MicroPython · Interface 14 pinos (I²C/UART/SPI/GPIO/PWM) |
| **LEDs e Sensores Topo** | Matriz LED **8×8** (vermelho/azul) · LED RGB (0–255) · Sensor infravermelho **ToF** (até `1,2 m` interior) |
| **Câmara** | `5 MP` foto · vídeo HD `720p @ 30 fps` · FOV `82,6°` |
| **Bateria e Autonomia** | LiPo `3,8 V · 1100 mAh` · `~8 min` com módulo ESP32 (até `13 min` sem módulos em condições ideais) |
| **Conectividade** | Wi-Fi dual-band `2,4 GHz` e `5,8 GHz` · Modos **AP** (direto) e **Station** (enxame até 16 drones) |
| **SDK 3.0 (UDP)** | IP direto `192.168.10.1` · Comandos porta `8889` · Estado `8890` · Fluxo vídeo `11111` |

---

## 2. Regras de Ouro de Segurança (Obrigatórias)

1. **Protetores sempre montados:** nunca descolar sem os 4 protetores nem com hélices rachadas ou dobradas.
2. **Apenas interiores sem vento:** mínimo `3 × 3 m` livres, janelas fechadas, sem ventoinhas/ar condicionado forte.
3. **Zero mãos no ar:** nunca agarrar o drone com hélices a rodar; manter distância de rostos e prender cabelos compridos. Usar `land` ou `emergency`.
4. **Iluminação e piso com contraste:** os sensores óticos inferiores precisam de luz e textura (evitar pisos pretos lisos ou espelhados).
5. **Desligar entre testes:** o drone arrefece com as hélices; deixá-lo ligado parado na mesa provoca sobreaquecimento. Nunca carregar baterias quentes ou inchadas.
6. **Segurança no código Python:** envolver o voo em `try / finally: tello.land()` e limitar movimentos iniciais a `30–80 cm`.

---

## 3. LED Frontal da Aeronave (Diagnóstico)

- **Verde (2 piscadelas periódicas):** sistema de visão inferior OK — pronto a voar.
- **Roxo lento:** SDK 3.0 ligado. **Roxo rápido:** sem comandos SDK há > 15 s.
- **Amarelo lento:** sem posicionamento ótico (ATTI — dar mais luz/contraste ao chão).
- **Amarelo rápido:** sem sinal Wi-Fi / à espera de ligação.
- **Vermelho a piscar (lento/rápido):** bateria baixa / crítica → aterrar imediatamente e trocar bateria.
- **Vermelho fixo:** erro crítico ou drone inclinado no arranque → desligar, nivelar e reiniciar.

---

## 4. Comandos Essenciais SDK 3.0 & Programação

- **Ativar SDK (obrigatório primeiro):** `command`
- **Voo básico:** `takeoff`, `land`, `emergency`, `forward 50`, `back 50`, `left 50`, `right 50`, `up 40`, `down 40`, `cw 90`, `ccw 90`, `battery?`
- **Módulo ESP32 — LED RGB:** `EXT led r g b` (0–255) · pulsar: `EXT led br t r g b`
- **Módulo ESP32 — Matriz 8×8:** `EXT mled l b 2 CTE` (direção `l/r/u/d`, cor `r/b/p`, velocidade, texto) · grelha: `EXT mled g <64 chars>`
- **Sensor ToF:** `EXT tof?` (devolve distância em mm até ~1200 mm)
- **Mission Pads (IDs 1–12):** `mon`, `mdirection 0`, `go x y z speed m1`, `jump x y z speed yaw m1 m2`
- **Ambientes:** **Mind+** (blocos online + MicroPython/Arduino offline) e **Python** (`pip install djitellopy`).

---

## 5. Resolução Rápida de Problemas (10 Casos)

1. **Não liga:** encaixar bateria até ao clique e carregar ≥ 15 min com bateria fria.
2. **Wi-Fi não aparece:** confirmar interruptor ESP32 em **AP**; se necessário, manter botão de energia ~5 s para repor Wi-Fi.
3. **Python/Mind+ sem resposta:** ligar apenas ao Wi-Fi do drone (sem VPN), permitir porta UDP `8889` na Firewall Windows, enviar `command` primeiro.
4. **Deriva / LED amarelo lento:** dar mais luz, fechar janelas/ventoinhas, usar padrão ou Mission Pads no chão, limpar sensores inferiores a seco.
5. **Vira-se ao descolar:** hélices A/B trocadas nos braços diagonais ou hélice partida → parar, desligar e corrigir pares marcados/não marcados.
6. **Não descola:** bateria < 20%, drone quente ou piso inclinado.
7. **Aterra sozinho:** bateria crítica, sobreaquecimento ou > 15 s sem comandos SDK.
8. **Matriz 8×8 não acende:** reencaixar cabo micro-USB do módulo ESP32 e testar `EXT led 0 255 0`.
9. **Não lê Mission Pads:** enviar `mon` e `mdirection 0`, voar entre 0,4 e 1,0 m com boa luz.
10. **LED vermelho fixo:** desligar, nivelar e reiniciar; se persistir, retirar kit para o CTE.

---

## 6. Checklist de Devolução (`INV-144` · Armário `D1.4C-MF-A04`)

1. Drone aterrado, **desligado** (LEDs apagados) e bateria arrefecida.
2. **4 protetores montados** e **4 hélices intactas** (sem fissuras nem cabelos nos eixos).
3. Módulo ESP32/8×8 bem encaixado e interruptor devolvido ao modo **AP**.
4. Kit completo conferido (drone, bateria 1100 mAh, módulo ESP32, cabo USB e Mission Pads).
5. Câmara e sensores inferiores limpos apenas com pano seco.
6. Comunicar ao CTE o **n.º do kit (1–10)**, bateria descarregada ou qualquer colisão/dano.

---

## 7. Prompts Prontos para o NotebookLM

### Prompt de Sistema / Instruções Personalizadas
> "Atua como Assistente Técnico e Pedagógico do CTE Informático para os drones DJI RoboMaster TT (Tello Talent, INV-144). Responde sempre em português europeu (PT-PT), de forma clara, curta e segura. Reforça sempre o uso exclusivo em interiores com os 4 protetores montados, distância de rostos/cabelos, desligamento entre edições de código e uso de try/finally com land() em Python. Nunca inventes palavras-passe de redes Wi-Fi da escola."
