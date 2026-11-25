# Base de Conhecimento — Painéis Interativos Promethean ActivPanel LX (65") (CTE Informático)

> **Documento-fonte mestre para o Google NotebookLM**
> Equipamento: **Painel Interativo Promethean ActivPanel LX (65") com OPS-A (Android EDLA) e gestão MDM**
> Inventário CTE: **INV-186** (6 unidades completas) · Suportes móveis nos estúdios: **INV-191** (Reflecta 105P-Shelf)
> Localização: **Estúdio STEM (1), Estúdio TEC1 (1), Estúdio TEC2 (1), Estúdio Hardware D3 (1), Oficinas O1 (1) e O3 (1)**
> Versão: 1.0 (novembro de 2026) · Língua: Português Europeu (PT-PT)

---

## 1. Resumo do Equipamento e Especificações Oficiais

- **Ecrã:** 65 polegadas TFT LCD (Direct LED), resolução **4K Ultra HD (3840 × 2160 @ 60 Hz)**, brilho típico 350–400 cd/m², contraste 1200:1, tempo de resposta 8 ms, ângulo de visão 178°.
- **Vidro e tecnologia tátil:** Vidro temperado antirreflexo de 3,2 mm com **Vellum Touch Technology** (até **20 pontos de toque simultâneos**), diferenciação entre caneta e dedo, rejeição de palma e apagamento intuitivo com a palma da mão.
- **Acessórios incluídos em cada sala:** **2 canetas passivas Promethean** (sem pilhas nem emparelhamento, pousadas na bandeja magnética frontal) e **1 comando à distância IR**.
- **Áudio:** 2 colunas frontais integradas de **15 W** cada (30 W total) + entrada/saída de áudio 3,5 mm na traseira.
- **Módulo computacional interno (OPS-A):** Computador encaixável na ranhura traseira Intel OPS com **Android 12 certificado pela Google (EDLA)** — acesso direto a Google Play, Chrome, Drive, Docs, Slides, Meet, YouTube e ferramentas educativas Promethean (**Whiteboard / Explain Everything**, **Annotate**, **Screen Capture**, **Screen Share**, **Timer**, **Spinner** e **HDMI App**).
- **Gestão centralizada (MDM):** Lote adquirido com gestão remota de painéis (compatível com **Promethean Admin Tools**, **Radix VISO MDM** e **Google Admin**).
- **Portas frontais (acesso rápido):**
  - **1× USB-C 2.0:** vídeo + áudio + toque interativo + **15 W Power Delivery** (1 único cabo faz tudo com portáteis compatíveis com vídeo/DP Alt Mode).
  - **1× HDMI 2.0** (vídeo + áudio — **não** passa toque sozinho!).
  - **1× USB-B 2.0 (Touch)** (obrigatório ligar em conjunto com o HDMI frontal para ter controlo tátil no portátil).
  - **1× USB-A 2.0** (pen USB ou periféricos).
- **Portas traseiras:** 2× HDMI 2.0, 2× USB-B (Touch), 1× USB-A 2.0, 1× VGA, Áudio 3,5 mm In/Out, RS-232, **LAN Ethernet RJ45 In & Out** (pass-through direto para o módulo OPS-A) e ranhura OPS.
- **Dimensões, peso e energia:** 1482 × 899 × 110 mm · **36,6 kg** · VESA 600 × 400 mm · 100–240 V AC · consumo típico ~106 W · **Standby <= 0,5 W** · arrefecimento silencioso sem ventoinha.

---

## 2. Controlos Físicos e Indicadores LED

### 2.1 Botões da consola frontal central
1. **Energia (Power + LED):** 1 toque curto liga o painel ou coloca em **Standby** (LED vermelho fixo).
2. **Seleção de Fonte (Input):** alterna entre **OPS (Android)**, **USB-C**, **HDMI Frontal**, **HDMI 1/2 Traseiro** e **VGA**.
3. **Volume (&minus;) / Volume (+):** ajusta o som das colunas frontais (2× 15 W).
4. **Congelar Ecrã (Freeze):** congela a imagem atual no painel (útil para trabalhar no portátil sem projetar); voltar a premir para descongelar.
5. **Definições (Settings / OSD):** abre o menu rápido de brilho, imagem, som e sistema.

### 2.2 Interruptor físico traseiro (`I / O`)
Localizado junto à entrada do cabo de alimentação AC na parte traseira:
- **Posição `I` (Ligado):** fornece corrente ao painel; o LED frontal fica **vermelho fixo (Standby)** pronto a ligar.
- **Posição `O` (Desligado):** corta totalmente a corrente; o LED frontal fica **completamente apagado**. *Não usar no dia a dia a quente — reservar para manutenção, limpeza com produto ou Hard Power Reset.*

### 2.3 Significado dos LEDs do botão de energia
- **Azul / Branco fixo:** Painel ligado e ativo. Se o ecrã estiver preto, selecionar a fonte correta (OPS / HDMI / USB-C).
- **Vermelho fixo:** Modo Standby (normal entre aulas). Premir Energia 1 vez para acordar.
- **A pulsar / piscar:** Painel a acordar, a arrancar o módulo OPS-A ou a instalar atualização MDM — aguardar 30–60 s sem cortar corrente.
- **Âmbar / Sem sinal:** Entrada ativa sem sinal de vídeo — acordar portátil (`Win + P`) ou mudar fonte para OPS.
- **Vermelho a piscar rápido:** Alerta de alimentação/arranque — executar *Hard Power Reset* de 60 s ou avisar equipa CTE.
- **Apagado (sem luz):** Sem corrente elétrica — confirmar tomada, encaixe do cabo AC e interruptor traseiro em `I`.

---

## 3. Regras de Ouro e Cuidados Críticos (CTE · INV-186)

1. **Apenas dedo ou canetas Promethean:** NUNCA usar marcadores de quadro branco reais, esferográficas, lápis ou objetos metálicos no vidro.
2. **Limpeza segura (zero sprays diretos):** Nunca pulverizar líquidos diretamente no ecrã (escorrem para a moldura tátil infravermelha!). Para o dia a dia usar microfibra seca. Para limpeza técnica (equipa CTE): desligar da tomada e usar pano de microfibra levemente humedecido com álcool isopropílico ou etanol 70–90%, secando de seguida.
3. **Suportes móveis com rodas (`INV-191`):** Manter sempre os travões das rodas bloqueados durante a aula. Antes de mover um painel (36,6 kg), **desligar primeiro todos os cabos** (corrente, rede, HDMI) e mover sempre com **2 adultos** pela estrutura, nunca empurrando o vidro.
4. **Standby no fim da aula (não cortar a quente):** Premir o botão Energia (consola ou comando IR) até o LED ficar vermelho fixo. Nunca desligar o interruptor traseiro `I/O` nem retirar o módulo OPS-A com o painel ligado.
5. **Privacidade em equipamento partilhado:** Se iniciar sessão com conta Google no OPS-A (Drive, Chrome, Classroom), **terminar sempre a sessão** antes de sair da sala.
6. **Moldura interior limpa:** Não colar post-its, fita-cola nem imãs nos cantos internos da moldura do ecrã (sensores infravermelhos de toque).

---

## 4. Ligar Portáteis e Espelhar Ecrãs (Passo a Passo)

### 4.1 Por cabo USB-C (1 cabo faz tudo)
1. Ligar um cabo **USB-C compatível com vídeo/dados (DP Alt Mode)** entre o portátil e a porta USB-C frontal (cabos finos só de carga de telemóvel não passam vídeo).
2. Passa simultaneamente imagem 4K, som, toque interativo e carga lenta 15 W.
3. Selecionar a entrada **USB-C** no botão Fonte da consola frontal.

### 4.2 Por cabo HDMI + USB-B Touch
1. Ligar o cabo **HDMI** à porta HDMI frontal (ou HDMI 1/2 traseiro).
2. **Para ter toque no portátil:** ligar obrigatoriamente também o cabo **USB-B (Touch)** da porta pareada ao HDMI até uma porta USB do portátil.
3. Selecionar a entrada **HDMI** correspondente. No Windows premir `Win + P` (Duplicar ou Estender) e selecionar *ActivPanel / HDMI* como dispositivo de saída de som.

### 4.3 Espelhamento sem fios (Promethean Screen Share no OPS-A)
1. Na entrada **OPS**, abrir a app **Screen Share** — aparece o **código de 6 dígitos (Panel ID)**.
2. No portátil (app **Screen Share Sender** em `share.mypromethean.com`) ou tablet/telemóvel (app **Promethean**), introduzir o código de 6 dígitos e o nome (sem login obrigatório).
3. **Sala de Espera (Waiting Room):** o professor aprova no painel quem entra no ecrã (suporta até **4 ecrãs em simultâneo** e **Touchback** em Windows/macOS).
4. Também suporta **AirPlay** (iPads `INV-178` / macOS) e **Miracast** (`Win + K`) consoante a configuração da rede Wi-Fi escolar. Em caso de congestionamento da rede, usar cabo USB-C ou HDMI frontal como Plano B imediato.

---

## 5. Resolução Rápida de Problemas (10 Casos)

1. **Painel não liga / LED apagado:** Confirmar tomada, cabo AC atrás do painel e interruptor traseiro na posição `I` (o LED deve acender a vermelho fixo).
2. **LED vermelho fixo e não acorda:** Premir o botão físico Energia na consola frontal (pilhas do comando IR podem estar gastas). Se não reagir, fazer *Hard Power Reset* de 60 s.
3. **«Sem sinal» ao ligar portátil:** Confirmar entrada exata no botão Fonte (USB-C / HDMI), premir `Win + P` (Duplicar/Estender) e garantir que o cabo USB-C suporta vídeo (não usar cabo só de carregamento).
4. **Imagem OK do PC, mas sem toque:** Falta ligar o cabo **USB-B (Touch)** junto ao HDMI escolhido — ou trocar por 1 cabo USB-C completo.
5. **Imagem congelada no ecrã:** Foi premido o botão **Freeze** na consola frontal ou comando IR — voltar a premir **Freeze**.
6. **Sem som nas colunas frontais:** Subir volume (`+`) na consola, escolher saída de som *ActivPanel / HDMI / USB-C* no portátil e verificar se não há jack ligado na saída 3,5 mm traseira.
7. **Screen Share / AirPlay não liga:** Confirmar código de 6 dígitos atual, rede Wi-Fi escolar sem isolamento de clientes, aprovar pedido na **Sala de Espera**, limpar cache da app Screen Share ou usar cabo USB-C/HDMI.
8. **OPS-A (Android) não aparece:** Premir Fonte e escolher **OPS**; aguardar até 30 s. Se continuar sem imagem, fazer *Hard Power Reset* de 60 s (e, pela equipa CTE desligado da corrente, verificar encaixe do módulo OPS-A).
9. **Caneta/toque falha ou escreve ao lado:** Limpar poeira/papéis/autocolantes dos 4 cantos internos da moldura tátil IR, reduzir sol direto no vidro e confirmar resolução 16:9 no portátil.
10. **Painel bloqueado, lento ou restrito por MDM:** Executar *Hard Power Reset* (interruptor em `O` → retirar da tomada **60 segundos** → religar em `I`). Se houver bloqueio MDM, contactar equipa do CTE.

---

## 6. Checklist de Fim de Aula (6 Pontos)

1. **Contas encerradas (OPS-A):** Terminar sessão no Google Drive, Chrome e Classroom.
2. **Quadro guardado e limpo:** Exportar anotações importantes (PDF/Drive) e fechar janelas temporárias.
3. **Cabos arrumados sem tensão:** Desligar portáteis pela ficha rígida (USB-C / HDMI / USB Touch).
4. **Acessórios no lugar:** 2 canetas passivas na bandeja magnética frontal e comando IR no suporte.
5. **Standby e suporte travado:** Painel em **Standby** (LED vermelho fixo) e travões das rodas (`INV-191`) bloqueados.
6. **Aviso ao CTE:** Comunicar falhas, danos ou canetas em falta indicando a sala exata (`STEM`, `TEC1`, `TEC2`, `D3`, `O1` ou `O3`).

---

## 7. Prompt de Sistema Pronto a Usar no Google NotebookLM

Copie e cole as instruções abaixo ao criar o caderno NotebookLM dedicado aos **Painéis Interativos Promethean ActivPanel LX**:

```text
És o Assistente Técnico e Pedagógico do CTE Informático para os 6 Painéis Interativos Promethean ActivPanel LX (65") com módulo OPS-A (Android EDLA) e gestão MDM (Inventário INV-186, instalados nos Estúdios STEM, TEC1, TEC2, Hardware D3 e Oficinas O1 e O3).

Regras obrigatórias de resposta:
1. Responde sempre em Português Europeu (PT-PT), de forma clara, prática e em passos curtos para professores e alunos durante a aula.
2. Baseia-te EXCLUSIVAMENTE nos documentos carregados neste caderno. Nunca inventes portas, teclas, palavras-passe escolares, contas MDM ou especificações.
3. Reforça sempre as 5 regras críticas do ActivPanel LX no CTE:
   - Escrever apenas com o dedo ou com as 2 canetas passivas Promethean (NUNCA marcadores reais de quadro branco nem objetos metálicos);
   - Nunca pulverizar líquidos diretamente no ecrã (usar apenas microfibra seca no dia a dia; limpeza com IPA/etanol 70–90% só pela equipa CTE com o painel desligado da tomada);
   - Para ter toque num portátil ligado por HDMI é obrigatório ligar também o cabo USB-B Touch (ou usar 1 único cabo USB-C compatível com vídeo/dados);
   - No fim da aula, terminar sempre sessões Google no OPS-A, pousar as 2 canetas na bandeja e colocar o painel em Standby (LED vermelho) — não cortar a corrente no interruptor traseiro I/O a quente;
   - Nos suportes móveis com rodas (INV-191), manter os travões bloqueados e desligar todos os cabos antes de mover o painel (36,6 kg, sempre com 2 adultos).
4. Quando o utilizador reportar "ecrã parado", verifica logo se o botão Freeze foi premido; se o LED estiver apagado, manda confirmar tomada e interruptor traseiro I/O; se o Screen Share falhar, lembra a Sala de Espera e o Plano B por cabo USB-C/HDMI.
5. Se houver vidro estalado, infiltração de líquido, cheiro a queimado, suporte móvel instável ou falha persistente após Hard Power Reset (60 s desligado da tomada), instrui a parar de imediato e contactar o docente responsável / equipa CTE indicando a sala (STEM, TEC1, TEC2, D3, O1 ou O3).
```
