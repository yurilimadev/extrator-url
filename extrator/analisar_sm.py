import requests
import streamlit as st
from usp.tree import sitemap_tree_for_homepage



def extrair_sitemap(url):
    tree = sitemap_tree_for_homepage(url)
    sitemap = []
    print(f'EXTRAINDO SITEMAP de {url}')
    for page in tree.all_pages():
        sitemap.append(page.url)
    return sitemap

def analisar(url):
    payload = {
        "chatInput": f"Analise para mim esse resultado de sitemap para ter uma ideia do funil de vendas desse site. SITEMAP: {extrair_sitemap(url)}",
        #"timestamp": st.session_state.get('time', 'N/A') # Exemplo de outro dado
    }
    try:
        # 3. Enviar a solicitação HTTP POST para o n8n
        # timeout é importante para evitar que o app trave
        with st.spinner('Aguardando resposta do n8n...'):
            response = requests.post(
                'https://primary-production-85b2.up.railway.app/webhook/95253fc1-c62d-4656-889b-dc8821dd5fb9', 
                json=payload, 
                timeout=30 # Tempo limite em segundos
            )
            
        # Verificar se a chamada foi bem-sucedida (código 200)
        if response.status_code == 200:
            # 4. Receber e processar a resposta do n8n
            data_response = response.json()
            
            st.success(f"Status da Resposta: {data_response.get('status')}")
            st.write("---")
            st.subheader("Resultado Recebido:")
            st.markdown(data_response['funil_de_vendas']) # Exibe o JSON completo

        else:
            st.error(f"Erro na chamada do n8n. Status Code: {response.status_code}")
            st.text(response.text) # Exibe o erro retornado
            
    except requests.exceptions.Timeout:
        st.error("O tempo limite da requisição foi excedido. Tente novamente.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    #print(extrair_sitemap('https://www.vendatodosantodia.com.br/'))
    teste_webhook('https://primary-production-85b2.up.railway.app/webhook-test/95253fc1-c62d-4656-889b-dc8821dd5fb9','https://www.vendatodosantodia.com.br/')