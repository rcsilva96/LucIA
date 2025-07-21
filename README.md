# LucIA - Assistente Pessoal em Python

![LucIA](assets/image/lucia.jpg)

LucIA é uma assistente pessoal em Python, modular e extensível, que responde por voz, entende comandos e executa tarefas no seu computador — desde abrir programas até ajudar com finanças e lembretes.

---

## 🚀 Funcionalidades

- Reconhecimento e síntese de voz com Python (SpeechRecognition, pyttsx3).  
- Modularidade com skills específicas (finanças, persona, lembretes).  
- Interface gráfica simples com avatar para feedback visual.  
- Comandos para abrir programas, pesquisar na internet, escrever texto, etc.  
- Respostas naturais e personalizadas (exemplo: respostas variadas para agradecimentos).  

---

## ⚙️ Como rodar

1. Clone o repositório  
```bash
git clone https://github.com/rcsilva96/lucia.git
cd lucia
```

2. Crie e ative um ambiente virtual (recomendado)  
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

3. Instale as dependências  
```bash
pip install -r requirements.txt
```

4. Execute o programa  
```bash
python main.py
```

---

## 🗂 Estrutura do projeto

```
lucia/
├── assets/            # Imagens, sons e outros arquivos estáticos
├── core/              # Código principal do motor de voz e comandos
├── interface/         # Código da interface gráfica (avatar, janelas)
├── skills/            # Funcionalidades modulares (finanças, persona, lembretes)
├── test/              # Testes diversos
├── main.py            # Script principal para rodar a assistente
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

---

## 🤝 Como contribuir

1. Faça um fork do projeto  
2. Crie uma branch com a feature (`git checkout -b feature/nova-funcionalidade`)  
3. Faça seus commits (`git commit -m 'Minha nova feature'`)  
4. Envie para o branch original (`git push origin feature/nova-funcionalidade`)  
5. Abra um Pull Request  

---

## 📞 Contato

Renato Silva  
https://www.linkedin.com/in/silva-renato-carvalho/

---

### Licença

MIT License © 2025 Renato Carvalho Silva

---

*LucIA: a assistente que entende você e seu código.*
