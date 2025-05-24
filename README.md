
# 🌾 Sistema de Irrigação Inteligente - Gestão Agrícola

Este projeto foi desenvolvido como parte das atividades práticas das fases do primeiro ano do curso de IA da FIAP. O objetivo é simular um sistema de gestão agrícola inteligente com funcionalidades de monitoramento climático, controle de irrigação, análise de dados e visão computacional para auxílio na tomada de decisões no campo.


## 📁 Estrutura do Projeto

```
src/
├── main.py          # Interface principal do Streamlit
├── fase_1.py        # Gestão de plantio 
├── fase_2.py        # Cadastro e análise de temperatura/umidade (SQLite)
├── fase_3.py        # Simulação de sensores (DHT22, PIR, LDR, HC-SR04)
├── fase_4.py        # Analise de dados com machine learning
├── fase_5.py        # Clusterização com KMeans e visualização
├── fase_6.py        # Detecção de objetos com YOLOv5 
```

---

## 🚀 Como Executar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Rode a aplicação

```bash
streamlit run src/main.py
```

---

## ✅ Melhorias nos projetos==

Os projetos agora tem uma visualzação unificada, utilizando streamlit agora todos os projetos podem ser acessados via dashboard
