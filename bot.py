import time
import os
from atproto import Client
from dotenv import load_dotenv


client = Client()

# Carrega as variaveis de ambiente
load_dotenv()

def main():
    try:
        # Login com o @ ou o email da conta.
        client.login(os.getenv('BSKY_LOGIN'), os.getenv('BSKY_PASS'))

        while True:
            notifications_response = client.app.bsky.notification.list_notifications()

            # Acessa as notificações, apenas elas.
            if notifications_response and hasattr(notifications_response, 'notifications'):
                notifications = notifications_response.notifications

                for notification in notifications:
                    if notification.reason == 'mention':
                        post_uri = notification.uri
                        post_cid = notification.cid

                        try:
                            client.like(uri=post_uri, cid=post_cid).uri
                        except Exception as e:
                            print(f"Erro ao dar like: {e}")

                        try:
                            client.repost(uri=post_uri,cid=post_cid).uri
                        except Exception as e:
                            print(f"Erro ao repostar: {e}")

            # Aguarde 60 segundos antes de verificar novamente
            time.sleep(60)

    except Exception as e:
        print(f"Erro na autenticação ou execução: {e}")

main()
