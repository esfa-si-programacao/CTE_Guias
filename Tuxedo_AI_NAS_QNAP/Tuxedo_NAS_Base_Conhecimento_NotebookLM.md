# Base de Conhecimento — Estação de Trabalho AI (Tuxedo Atlas XL) e NAS QNAP TVS-h874 (CTE Informático)

> **Documento-fonte mestre para o Google NotebookLM**
> Equipamentos: **Estação de Trabalho AI TUXEDO Atlas XL (Gen1 Intel) · Servidor NAS QNAP TVS-h874 (Core i7 · 32 GB) · UPS APC Smart-UPS SMT LCD**
> Inventário CTE: **INV-006** (Tuxedo Atlas XL) + **INV-223** (NAS QNAP TVS-h874) + **INV-224** (UPS APC Smart-UPS)
> Localização: **Estúdio 4C** (NAS e UPS instalados junto ao servidor/bastidor)
> Versão: 1.0 (novembro de 2026) · Língua: Português Europeu (PT-PT)

---

## 1. Resumo da Infraestrutura e Especificações Oficiais

### 1.1 Estação de Trabalho AI — TUXEDO Atlas XL (Gen1 Intel) (`INV-006`)
- **Chassis e fluxo de ar:** Torre ATX estilo **Fractal Design North XL** (447 × 215 × 469 mm) com ripas frontais em madeira natural certificada e painéis em malha (*mesh*) de alto fluxo de ar; topo com botão Power e portas USB-A / USB-C.
- **Plataforma:** Motherboard Intel Z790, processador Intel Core (13.ª/14.ª Geração) com arrefecimento líquido AiO (240/280 mm), memória DDR5 dual-channel, armazenamento SSD M.2 NVMe PCIe 4.0 e fonte 80+ Gold.
- **Aceleração GPU:** Placa gráfica dedicada de alto desempenho para Inteligência Artificial, *Machine Learning*, Processamento de Linguagem Natural (LLMs locais), Visão Computacional e conversão/renderização de vídeo (suporte NVIDIA CUDA / Tensor Cores).
- **Sistema Operativo e Software:** **TUXEDO OS / Ubuntu Linux** com **TUXEDO Control Center**, drivers NVIDIA/CUDA, Python 3, PyTorch, Ollama (execução local de LLMs), JupyterLab, Git e Docker.

### 1.2 Servidor NAS e Virtualização — QNAP TVS-h874-i7-32G (`INV-223`)
- **Processador e memória:** **Intel Core i7-12700E** (12 núcleos: 8P + 4E, 20 threads, até 4,8 GHz), gráficos Intel UHD 770 e **32 GB DDR4 RAM** (2× 16 GB SODIMM, expansível até 64 GB).
- **Armazenamento:** **8 baías frontais 3,5"/2,5" SATA 6 Gb/s (*hot-swap*)** com fecho de chave + **2 ranhuras internas M.2 2280 PCIe Gen4 x4 NVMe**.
- **Conetividade e expansão:** **2 portas de rede 2,5 GbE RJ45** (suporta *Port Trunking* / agregação e *failover*), 2 ranhuras PCIe Gen4 (x16 + x4), 1 saída HDMI 1.4b (4K 30 Hz) e portas USB 3.2 Gen2 (10 Gbps).
- **Sistema Operativo QuTS hero (ZFS):** Sistema de ficheiros **ZFS de 128 bits** com verificação e reparação automática de corrupção silenciosa (*self-healing*), compressão e deduplicação *inline*, Reciclagem de Rede (`@Recycle`) e **Snapshots instantâneos** contra apagamento acidental ou *ransomware*.
- **Virtualização integrada:** **Virtualization Station** (máquinas virtuais Linux/Windows acedidas via navegador pelos portáteis e MacBooks do CTE) e **Container Station** (contentores Docker / LXD).

### 1.3 Proteção Elétrica — UPS APC Smart-UPS SMT LCD RM SmartConnect (`INV-224`)
- Unidade de alimentação ininterrupta (UPS) instalada junto ao servidor no Estúdio 4C.
- Protege o servidor NAS QNAP contra cortes de energia e picos de tensão, comunicando via USB/rede para ordenar o encerramento seguro (*graceful shutdown*) do sistema ZFS e das máquinas virtuais caso a falha elétrica se prolongue.

---

## 2. 5 Regras de Ouro de Utilização Partilhada e Segurança

1. **Nunca desligar o servidor NAS nem a UPS (Operação 24/7):** O QNAP TVS-h874 (`INV-223`) e a UPS APC (`INV-224`) servem toda a escola 24 horas por dia. Nunca prima o botão Power do NAS, nunca desligue o interruptor da UPS e nunca retire cabos de rede RJ45. No final da aula, faça apenas **Logout** da sua sessão.
2. **Proibido abrir ou puxar as 8 gavetas de disco do NAS:** Embora as baías SATA sejam *hot-swap*, retirar uma gaveta em funcionamento degrada imediatamente o *pool* RAID/ZFS e obriga a uma reconstrução (*resilvering*) demorada. As gavetas devem permanecer trancadas e só podem ser manuseadas pela equipa técnica do CTE.
3. **Partilha justa de GPU/VRAM na Tuxedo Atlas XL:** Antes de iniciar um treino PyTorch ou carregar um LLM, execute sempre `nvidia-smi` no terminal para verificar se a GPU está livre. Quando terminar a aula, feche obrigatoriamente os seus *kernels* Jupyter (*Kernel → Shut Down Kernel*) para libertar a VRAM para a turma seguinte.
4. **Zero `sudo pip` no sistema Linux global:** Nunca instale pacotes Python globalmente com `sudo pip` nem `--break-system-packages` (pode corromper drivers CUDA/PyTorch de outras turmas). Crie e ative sempre um ambiente virtual (`python3 -m venv .venv && source .venv/bin/activate`) dentro da pasta do seu grupo.
5. **Fluxo de ar livre e backups no NAS:** Nunca pouse mochilas, casacos ou cadernos sobre o topo ou encostados à frente em madeira/malha da Tuxedo Atlas XL nem às grelhas do NAS QNAP. Guarde sempre o código final, datasets e pesos validados na pasta da turma no NAS QNAP (protegida por ZFS), limpando ficheiros temporários de `/tmp`.

---

## 3. Comandos Essenciais e Acesso aos Serviços

| Tarefa | Comando / Endereço | Notas |
|---|---|---|
| **Ver estado da GPU e VRAM** | `nvidia-smi` (ou `watch -n 2 nvidia-smi`) | Mostra memória VRAM livre/ocupada, temperatura e PIDs ativos na GPU. |
| **Criar e ativar ambiente Python** | `python3 -m venv .venv && source .venv/bin/activate` | Executar dentro da pasta de projeto do grupo antes de `pip install`. |
| **Listar e correr LLMs locais** | `ollama list` / `ollama run <modelo>` | API local disponível em `http://localhost:11434`. Escrever `/bye` para sair. |
| **Aceder por SSH à Tuxedo** | `ssh utilizador@<IP-Tuxedo>` | Usar a conta de aluno/grupo atribuída pelo docente no Estúdio 4C. |
| **Aceder à Virtualization Station (QNAP)** | `https://<IP-do-NAS>:8080` | Iniciar apenas a VM atribuída ao grupo e encerrá-la no fim se for temporária. |
| **Montar pasta partilhada SMB (2,5 GbE)** | Windows: `\\<IP-do-NAS>\<partilha>` · macOS/Linux: `smb://<IP-do-NAS>/<partilha>` | Guardar datasets finais, vídeos renderizados e backups do grupo. |

---

## 4. Tabela de LEDs e Alarmes (QNAP TVS-h874 e UPS APC)

| Indicador / Alarme | Significado | Ação Recomendada |
|---|---|---|
| **Status Verde fixo (NAS)** | Sistema QuTS hero e pools ZFS saudáveis | Operação normal. |
| **Status Verde / Vermelho alternado (NAS)** | Reconstrução RAID/ZFS (*resilvering*), formatação ou atualização de firmware | **CRÍTICO: Proibido desligar a energia ou tocar nas baías!** Aguardar conclusão. |
| **Status Vermelho fixo ou a piscar (NAS)** | Pool ZFS quase cheio (>90%), erro de disco, ventoinha ou temperatura | Não desligar o servidor; avisar imediatamente o docente/equipa CTE. |
| **LED HDD 1–8 ou M.2 a Vermelho** | Falha de leitura/escrita ou erro SMART nesse disco | **Não puxar a gaveta!** Comunicar ao CTE para substituição técnica *hot-swap*. |
| **LAN Laranja a piscar / USB Azul** | Tráfego ativo nas portas 2,5 GbE / dispositivo USB ligado | Normal; nunca desligar os cabos de rede RJ45. |
| **UPS APC (`INV-224`) a apitar / alerta LCD** | Corte de energia na sala (modo bateria), sobrecarga ou aviso de bateria | Guardar trabalho imediatamente, parar treinos pesados de GPU e avisar o CTE. |

---

## 5. Resolução Rápida de Problemas (10 Casos)

1. **Erro `CUDA out of memory`:** Verificar processos em `nvidia-smi`, encerrar *kernels* Jupyter inativos (*Shut Down Kernel*), reduzir o `batch_size` ou escolher um modelo quantizado (4-bit/8-bit).
2. **`nvidia-smi` falha (*Failed to initialize NVML*):** O kernel Linux atualizou sem recarregar o módulo NVIDIA. Confirmar que não há treinos ativos e pedir ao docente para reiniciar a Tuxedo (`sudo reboot`).
3. **Erro `externally-managed-environment` no `pip`:** Criar e ativar um ambiente virtual (`python3 -m venv .venv && source .venv/bin/activate`) na pasta do grupo; nunca usar `sudo pip`.
4. **LED Status Verde/Vermelho alternado no QNAP:** Reconstrução RAID/ZFS ou atualização em curso — proibido desligar ou mexer nos discos.
5. **LED de uma baía HDD 1–8 a vermelho:** Disco com falha SMART; não retirar a gaveta e avisar a equipa técnica do CTE.
6. **Escrita lenta no NAS ou alerta de Pool ZFS > 85%:** O ZFS precisa de ~15–20% de espaço livre para manter alto desempenho; limpar `@Recycle`, snapshots antigos ou VMs de módulos concluídos.
7. **Máquina Virtual lenta ou não arranca no QNAP:** Os 32 GB de RAM do QNAP estão saturados por demasiadas VMs abertas; encerrar ordenadamente as VMs de aulas anteriores que ficaram ligadas sem uso.
8. **Sem acesso SSH, JupyterLab ou pasta SMB:** Confirmar que o portátil está ligado à rede local do Estúdio 4C (e não a uma rede Wi-Fi de convidados isolada) e verificar se o IP não foi bloqueado pela firewall após palavras-passe erradas.
9. **Ventoinhas muito altas / aquecimento:** Retirar imediatamente mochilas, livros ou casacos de cima/frente da Tuxedo Atlas XL e das grelhas do NAS QNAP; verificar limpeza dos filtros de pó.
10. **Ficheiro apagado ou sobrescrito por engano numa pasta do NAS:** Não gravar novos ficheiros por cima; pedir ao docente para restaurar a partir da pasta `@Recycle` ou dos **Snapshots ZFS** do QuTS hero.

---

## 6. Checklist de Fim de Sessão (Estúdio 4C)

1. **VRAM / GPU libertada:** Kernels Jupyter e scripts PyTorch/Ollama de teste encerrados (`nvidia-smi` sem processos órfãos do grupo).
2. **Dados guardados no NAS:** Código, datasets e modelos finais copiados para a pasta da turma no QNAP e ficheiros temporários em `/tmp` removidos.
3. **VMs de aula suspensas:** Máquinas virtuais temporárias encerradas na *Virtualization Station* para libertar RAM do QNAP.
4. **Logout seguro (NAS e UPS 24/7):** Sessão local, SSH e consola web fechadas **sem desligar o QNAP TVS-h874 nem a UPS APC**.
5. **Ventilação livre:** Frente em madeira/malha e topo da Tuxedo Atlas XL e grelhas do NAS desobstruídos.
6. **Aviso ao CTE:** Comunicar qualquer LED vermelho no NAS, alarme sonoro na UPS APC ou anomalia de GPU/rede.

---

## 7. Prompt de Sistema Pronto a Usar no Google NotebookLM

Copie e cole as instruções abaixo na configuração do caderno NotebookLM dedicado à **Estação AI Tuxedo Atlas XL & NAS QNAP TVS-h874**:

```text
És o Assistente Técnico e Pedagógico do CTE Informático para a infraestrutura de IA e Virtualização do Estúdio 4C: Estação de Trabalho AI TUXEDO Atlas XL (INV-006), Servidor NAS QNAP TVS-h874 i7 32 GB (INV-223) e UPS APC Smart-UPS (INV-224).

Regras obrigatórias de resposta:
1. Responde sempre em Português Europeu (PT-PT), com linguagem clara, rigorosa e estruturada em passos práticos para alunos e professores.
2. Baseia-te EXCLUSIVAMENTE nos documentos carregados neste caderno. Nunca inventes endereços IP, contas, palavras-passe de administração ou especificações não documentadas.
3. Prioriza sempre as 5 regras críticas de infraestrutura partilhada:
   - Nunca desligar o servidor NAS QNAP TVS-h874 nem a UPS APC (operam 24/7); fazer apenas Logout;
   - Nunca abrir nem retirar as 8 gavetas de disco SATA hot-swap do NAS (risco de degradação do pool ZFS);
   - Verificar sempre a ocupação da GPU/VRAM com `nvidia-smi` antes de iniciar treinos e fechar kernels Jupyter (`Shut Down Kernel`) no fim da aula;
   - Usar sempre ambientes virtuais Python (`python3 -m venv .venv`) na pasta do grupo — nunca usar `sudo pip`;
   - Manter o fluxo de ar da torre Tuxedo Atlas XL (North XL) e do NAS totalmente desobstruído e guardar backups/datasets finais na partilha ZFS do NAS.
4. Nunca sugiras comandos destrutivos (`rm -rf`, formatação de pools ZFS, alteração de drivers kernel NVIDIA por alunos ou remoção de discos).
5. Se houver LED vermelho no NAS (Status ou HDD 1–8), piscar verde/vermelho, alarme sonoro na UPS APC ou falha de hardware, instrui o utilizador a não desligar o equipamento e a contactar imediatamente o docente responsável ou a equipa técnica do CTE.
```
