# Bluebot

Este é um bot desenvolvido para interagir com a API do Bluesky usando a biblioteca `atproto`. O bot faz login na conta, verifica notificações de menções e dá like e repost em postagens mencionadas.

## Funcionalidade

- **Login:** O bot faz login na conta do Bluesky usando as credenciais fornecidas.
- **Notificações:** Verifica notificações a cada 60 segundos.
- **Interações:** Dá like e repost em postagens mencionadas.

## Dependências

Certifique-se de instalar as seguintes dependências para executar o bot:

- `atproto`
- `python-dotenv`

Você pode instalar as dependências usando o pip:

```bash
pip install atproto python-dotenv
````

## Configuração

Crie um arquivo .env na raiz do projeto.

Adicione suas credenciais da conta do Bluesky no arquivo .env:

**BSKY_LOGIN=seu_login_ou_email**

**BSKY_PASS=sua_senha**

## Uso

- `Clone este repositório.`

- `Instale as dependências mencionadas acima.`

- `Configure suas credenciais no arquivo .env.`

## Execute o bot:
```bash
python seu_arquivo.py
```
O bot começará a verificar as notificações e a interagir com as postagens mencionadas.

Copyright
© 2024 Sylvio Labriola. Todos os direitos reservados.
