# Base de Conhecimento — Scanner 3D Einstar (CTE Informático)

> **Documento-fonte mestre para o Google NotebookLM**
> Equipamento: **Scanner 3D Portátil Shining 3D Einstar**
> Inventário CTE: **INV-228** (2 unidades completas)
> Localização: **Estúdio SC - LMAS**
> Software dedicado: **EXStar** (Windows com GPU NVIDIA CUDA ou macOS Apple Silicon Pro)
> Versão: 1.0 (novembro de 2026) · Língua: Português Europeu (PT-PT)

---

## 1. Resumo do Equipamento e Especificações Oficiais

- **Tecnologia de digitalização:** Luz estruturada infravermelha (**IR VCSEL**) com certificação **Laser Classe 1 (*Eye-safe*)** — segura para os olhos, permitindo digitalizar rostos e pessoas sem encandeamento.
- **Distância de trabalho:** **160 mm a 1400 mm** · Distância ótima recomendada: **~400 mm**.
- **Distância entre pontos (*Point Distance*):** **0,1 mm a 3 mm** (ajuste no software consoante o detalhe necessário e a memória do computador).
- **Velocidade de captura:** até **14 fotogramas por segundo (fps)** (~980 000 pontos/segundo).
- **Campo de visão máximo (FOV):** **434 mm × 379 mm**.
- **Alinhamento / Rastreio:** Características (*Feature*), Híbrido (*Hybrid*), Textura (*Texture*) e Marcadores Globais (*Global Markers*, com suporte a ficheiros `.p3`).
- **Digitalização a cores:** Sim (câmara RGB de textura integrada).
- **Dimensões e peso:** **220 mm × 46 mm × 55 mm** · **500 g**.
- **Alimentação e ligação:** Cabo único proprietário na base do punho com ligação simultânea a **USB (dados para o computador)** e **fonte de alimentação externa 12 V / 5 A** (não funciona só por USB!).
- **Fixação em tripé:** Rosca padrão **1/4"-20 UNC** na base.
- **Formatos de exportação:** **STL** (malha sem cor para impressão 3D/CAD), **OBJ** (malha + textura `.jpg` + `.mtl`), **PLY** (malha com cor por vértice), **3MF** (impressão 3D moderna) e **ASC** (nuvem de pontos).

---

## 2. Requisitos de Computador (EXStar)

O software **EXStar** faz reconstrução 3D em tempo real e **não funciona em portáteis comuns sem gráfica dedicada**.

### 2.1 Windows (64-bit)
- **Sistema operativo:** Windows 10 ou Windows 11 (64-bit).
- **Placa gráfica (GPU):** **NVIDIA dedicada com suporte CUDA 10.2+** (obrigatório!).
  - *Mínimo (EXStar v1.2+):* NVIDIA GTX 1050 (**4 GB VRAM**), Intel Core i5-1240P+, **16 GB RAM**.
  - *Recomendado:* NVIDIA GTX 1060 / série RTX (**6 GB+ VRAM**), Intel Core i7-11800H+ (ou AMD equivalente), **32 GB+ RAM**.
- **Porta USB:** USB 2.0 ou superior (USB 3.0 recomendada para maior estabilidade).

### 2.2 macOS
- **Processador:** Apple Silicon **M1 Pro** ou superior (GPU 8-core+).
- **Sistema operativo:** macOS 13 (Ventura) ou mais recente.
- **Memória RAM:** **32 GB** recomendados (16 GB mínimo).

*(No CTE, o Estúdio SC - LMAS dispõe de 1× Apple MacBook Pro 16" M3 Pro com 36 GB RAM (`INV-068`); confirmar com o docente qual a estação de trabalho Windows/Mac designada na sala para o Einstar.)*

---

## 3. Controlos Físicos e Indicadores LED do Einstar

### 3.1 Botões traseiros do punho
- **Botão Central (Play / Scan / Pausa):** Inicia a pré-visualização, arranca a digitalização ou coloca em pausa.
  - *Duplo clique no botão central:* alterna os botões `+` / `-` entre **Zoom** e **Brilho/Exposição**.
- **Botão Superior (`+`):** Aumenta o zoom na vista 3D ou aumenta o brilho/exposição da câmara.
- **Botão Inferior (`-`):** Reduz o zoom ou diminui o brilho/exposição.

### 3.2 Indicadores LED
- **LED Indicador de Distância (feedback em tempo real):**
  - **Verde:** Distância de trabalho ideal (~400 mm) — manter nesta zona!
  - **Azul:** Scanner demasiado longe do objeto — aproximar ligeiramente.
  - **Vermelho / Amarelo:** Scanner demasiado perto do objeto — afastar ligeiramente.
- **LED de Estado / Energia:**
  - **Azul fixo:** Alimentação 12 V e ligação USB corretas; scanner pronto.
  - **Vermelho (fixo ou a piscar):** Erro de ligação USB, fonte 12 V desligada ou falha de comunicação.

---

## 4. Regras de Ouro e Cuidados Críticos (CTE · INV-228)

1. **Computador compatível + Fonte 12 V obrigatória:** O Einstar só funciona ligado à corrente elétrica (12 V / 5 A) **e** ao computador com GPU dedicada (NVIDIA CUDA ou Apple Silicon Pro).
2. **NUNCA trocar a placa de calibração entre os 2 kits (`INV-228`):** Cada placa de calibração tem parâmetros óticos associados ao **número de série único** do respetivo scanner. Trocar placas faz a calibração falhar ou degrada a precisão!
3. **Proteger cabo e ótica:** Encaixar o conector principal alinhado até travar, nunca dobrar o cabo junto à base durante o movimento e nunca tocar com os dedos nas lentes frontais nem riscar a placa de calibração (limpar só com pano macio/húmido, sem álcool nem solventes).
4. **Superfícies pretas, brilhantes ou transparentes:** A luz infravermelha é absorvida por objetos pretos e refletida por metal cromado ou vidro. Usar **marcadores autocolantes de forma aleatória** (nunca em linha reta!) ou, quando autorizado pelo docente em espaço ventilado, spray fosco removível.
5. **Segurança ao digitalizar pessoas (*Portrait Mode*):** Apesar de o laser IR ser **Classe 1 (seguro para os olhos)**, evitar olhar fixamente para o projetor a curta distância e pedir à pessoa retratada para permanecer imóvel e evitar óculos escuros/refletores.

---

## 5. Fluxo de Trabalho no Software EXStar (Passo a Passo)

1. **Ligar hardware:** Ligar primeiro o cabo USB + fonte 12 V/5 A ao scanner e só depois abrir o **EXStar** (confirmar LED azul de estado).
2. **Calibrar (se necessário):** Obrigatório na 1.ª utilização, após transporte/choque, se houver erros frequentes de alinhamento ou se passaram **mais de 14 dias** desde a última calibração. Usar **exclusivamente a placa do mesmo n.º de série** sobre mesa plana, sem luz solar direta, seguindo os 5 ângulos/alturas até os indicadores ficarem verdes.
3. **Criar novo projeto:** Escolher **Objeto (*Object*)** ou **Retrato (*Portrait*)**, selecionar tamanho aproximado, resolução (*Point Distance*, ex.: 0,2–0,5 mm para objetos médios; 0,5–1,0 mm para peças grandes/retratos) e modo de alinhamento (*Feature*, *Hybrid*, *Texture* ou *Global Markers*).
4. **Pré-visualizar e ajustar brilho:** Premir o botão central 1× para abrir a pré-visualização e ajustar o brilho até o objeto aparecer nítido sem zonas vermelhas saturadas (sobre-exposição).
5. **Digitalizar:** Premir o botão central para iniciar. Manter o LED na cor **Verde (~400 mm)**, mover lentamente à volta do objeto mantendo sempre sobreposição com a área já capturada. Se perder alinhamento (*Tracking Lost*), apontar para uma zona já digitalizada com detalhes para recuperar.
6. **Editar e gerar malha (*Mesh*):** Remover ruído de fundo (ex.: mesa) com a ferramenta de seleção/laço, clicar em **Generate Mesh** (escolher *Watertight* / estanque para impressão 3D ou *Unwatertight* para manter aberturas originais) e aplicar simplificação/suavização se necessário.
7. **Exportar:** Guardar no formato adequado:
   - **`.stl`** → Impressão 3D (Snapmaker 2.0 / Elegoo Neptune 4) e CAD;
   - **`.obj` ou `.ply`** → Modelos com cor/textura para Blender, Unity, WebXR ou apresentação;
   - **`.3mf`** → Impressão 3D moderna com metadados/cor;
   - **`.asc`** → Nuvem de pontos para análise métrica.

---

## 6. Resolução Rápida de Problemas (10 Casos)

1. **Scanner não liga / LED vermelho fixo:** Confirmar ligação à tomada (12 V/5 A) e que o conector na base do punho está bem encaixado; trocar de porta USB (preferir USB 3.0 direta na placa-mãe/portátil, sem hubs passivos).
2. **EXStar não arranca ou fecha ao abrir:** Verificar se o PC tem GPU NVIDIA CUDA (≥ 4 GB VRAM) com drivers atualizados ou Mac Apple Silicon Pro; portáteis com gráfica integrada básica não são suportados.
3. **Calibração falha repetidamente:** Confirmar se a placa de calibração corresponde ao n.º de série deste scanner (há 2 unidades `INV-228` no CTE!), limpar poeiras sem álcool e evitar luz solar direta.
4. **LED de distância sempre azul ou sempre vermelho:** Aproximar para ~400 mm (se azul) ou afastar (se vermelho/amarelo) até o indicador ficar **verde**.
5. **Objeto não aparece ou fica com buracos pretos:** Superfície muito escura, brilhante ou transparente — aumentar ligeiramente o brilho no punho (`+`) ou preparar a peça (marcadores/spray fosco autorizado).
6. **Perde o alinhamento (*Tracking Lost*) a toda a hora:** Movimento demasiado rápido ou peça lisa/simétrica — mover mais devagar mantendo áreas já capturadas no enquadramento, ou usar marcadores autocolantes em padrão **aleatório** (mínimo 4 visíveis ao mesmo tempo).
7. **Fundo da mesa fica digitalizado por baixo da peça:** Usar a função de recorte/laço antes de gerar a malha, ou colocar o objeto sobre um suporte ligeiramente elevado com marcadores na base.
8. **Computador fica lento / sem memória a meio do scan:** Aumentar o *Point Distance* (ex.: de 0,1 mm para 0,5 mm ou 1,0 mm) ao criar o projeto e fechar programas pesados em segundo plano.
9. **Modelo exportado em STL não tem cor:** Normal — o formato `.stl` só guarda geometria (triângulos). Para manter cor/textura, exportar em **`.obj`** (com `.jpg` e `.mtl`) ou **`.ply`**.
10. **Peça imprimiu na escala errada ou com furos na Snapmaker/Elegoo:** Verificar que o *Mesh* foi gerado em modo **Watertight (estanque)** e confirmar unidades em milímetros (`mm`) no software de fatiamento (Luban/OrcaSlicer/Cura).

---

## 7. Checklist de Devolução (Estúdio SC - LMAS · INV-228)

1. **Projeto guardado e exportado:** Ficheiros (`.stl` / `.obj` / `.ply`) copiados para a pasta da turma; apagar projetos pesados temporários no disco partilhado se aplicável.
2. **Scanner desligado com segurança:** Fechar o EXStar e desligar primeiro da corrente (12 V) e do USB sem puxar pelo cabo.
3. **Lentes e corpo limpos:** Sem dedadas nas câmaras frontais (usar apenas microfibra seca se necessário).
4. **Placa de calibração correta na bolsa:** Confirmar que a placa de calibração **do mesmo número de série** está riscada-zero e dentro da bolsa protetora.
5. **Kit completo no estojo (`INV-228`):** Scanner Einstar, cabo de dados/alimentação, adaptador 12 V/5 A, cabo de corrente, placa de calibração correspondente, folha(s) de marcadores e correia/mala.
6. **Aviso ao CTE:** Indicar qual das 2 unidades (`INV-228` #1 ou #2) foi usada, se faltam marcadores ou se houve queda/anomalia.

---

## 8. Prompt de Sistema Pronto a Usar no Google NotebookLM

Copie e cole as instruções abaixo na configuração do caderno NotebookLM dedicado ao **Scanner 3D Einstar**:

```text
És o Assistente Técnico e Pedagógico do CTE Informático para o Scanner 3D Portátil Shining 3D Einstar (Inventário INV-228, 2 unidades no Estúdio SC - LMAS) e software EXStar.

Regras obrigatórias de resposta:
1. Responde sempre em Português Europeu (PT-PT), com linguagem clara, direta e estruturada em passos curtos para alunos e professores.
2. Baseia-te EXCLUSIVAMENTE nos documentos carregados neste caderno. Nunca inventes especificações, teclas, compatibilidades de PCs da escola ou procedimentos.
3. Destaca sempre as 5 regras críticas do Einstar no CTE:
   - Exige PC com GPU dedicada (NVIDIA CUDA >= 4 GB VRAM ou Apple Silicon M1 Pro+) e alimentação 12 V/5 A ligada à tomada (não funciona só por USB);
   - NUNCA trocar a placa de calibração entre as 2 unidades INV-228 (cada placa é emparelhada ao número de série do scanner);
   - Manter a distância de trabalho na zona VERDE (~400 mm; azul = longe, vermelho = perto);
   - Superfícies pretas, espelhadas ou transparentes precisam de marcadores aleatórios (nunca em linha reta) ou spray fosco autorizado;
   - Exportar em STL (estanque / watertight) para impressão 3D, ou OBJ/PLY para manter cor e texturas.
4. Lembra aos alunos que os seus modelos 3D podem ser ligados a impressão 3D (Snapmaker 2.0 A350T ou Elegoo Neptune 4) ou Realidade Virtual (Meta Quest 3).
5. Se houver queda do scanner, dano no conector do cabo, risco na placa de calibração ou falha persistente (LED vermelho), instrui o utilizador a parar e entregar o kit ao docente ou equipa do CTE no Estúdio SC - LMAS.
```
