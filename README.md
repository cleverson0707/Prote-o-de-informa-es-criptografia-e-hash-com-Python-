# 🛡️ Simulador de Autenticação Segura e Força Bruta

Este é um projeto didático em Python desenvolvido para demonstrar na prática conceitos fundamentais de cibersegurança, criptografia hash e vulnerabilidades de senhas fracas.

## 🚀 Funcionalidades

- **Cálculo de Hashes Reais:** Utiliza o algoritmo **SHA-256** da biblioteca `hashlib` para mascarar as senhas.
- **Sistema de Login Seguro:** Demonstra como sistemas modernos autenticam usuários comparando hashes armazenados, garantindo que a senha original nunca fique exposta em texto limpo.
- **Simulador de Ataque de Força Bruta:** Utiliza a biblioteca `itertools` para gerar combinações sequenciais de caracteres (`itertools.product`), simulando como um atacante quebra senhas curtas ou previsíveis.

## 🧠 Conceitos Demonstrados

1. **Efeito Avalanche:** Como uma mudança mínima na entrada altera completamente o hash de saída.
2. **Armazenamento Seguro:** A importância de nunca salvar senhas em formato de texto limpo em bancos de dados.
3. **Complexidade de Senhas:** Demonstração visual de como o número de tentativas e o tempo crescem exponencialmente ao aumentar o tamanho da senha.

## 🛠️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `main.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python main.py
   ```

## 📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, estudar e modificar!
