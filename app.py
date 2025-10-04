import streamlit as st
import pandas as pd
from extrator.extrator_url import ExtratorURL
from extrator.analisar_sm import extrair_sitemap

st.markdown('''
    <style>
        .subHeader{
            background-color: green;
            padding: 2%;
            border-radius:5px;
            font-weight:700;
            transition: background-color 200ms ease-out 50ms, padding 200ms ease-out;
        }
        .subHeader:hover{
            background-color: rebeccapurple;
            padding: 3% 2%;
            
        }
    </style>
''', unsafe_allow_html=True)

st.set_page_config(
    page_title="Extrator URL",
    layout='centered'
)
# INICIO DA APLICAÇÃO
st.title(
    '🤓 Extrator URL 📊'
)
st.markdown(
    '''
    <p class="subHeader">
    Tenha uma pista da estrutura do funil de vendas de um produto digital.
    </p>
    ''',
    unsafe_allow_html=True
)

if 'url' not in st.session_state:
    st.session_state['url'] = ''
if 'dados_extraidos' not in st.session_state:
    st.session_state['dados_extraidos'] = None
if 'analisar_sitemap' not in st.session_state:
    st.session_state['analisar_sitemap'] = False

def limpar_input():
    st.session_state['url'] = ''
    st.session_state['dados_extraidos'] = None
    st.session_state['analisar_sitemap'] = False

def acao_extrair(url):
    try:
        url_use = ExtratorURL(url)
        url_base = url_use.get_url_base()
        parametros = url_use.get_url_parametros()
        
        dict_dir = url_use.get_diretorio_json()
        st.session_state['dados_extraidos'] = {
            'parametros': parametros,
            'dict_dir': dict_dir,
            'url_base': url_use.get_url_base()
        }
        st.session_state['analisar_sitemap'] = True
    except Exception as e:
        st.session_state['dados_extraidos'] = str(e) 
        st.session_state['analisar_sitemap'] = False

def analisar_sitemap():
    st.session_state['analisar_sitemap'] = True


url = st.text_input(
    'Insira a URL que deseja analisar',
    key='url',
)

opcoes_botoes = st.container(
    horizontal='left',
    horizontal_alignment='left'
)

with opcoes_botoes:
    botao_extrair = st.button('Extrair', on_click=acao_extrair, args=[url])
    botao_limpar = st.button('Limpar', on_click=limpar_input)

if st.session_state['dados_extraidos']:
    dados = st.session_state['dados_extraidos']
    if isinstance(dados, str):
        st.caption(dados)
    else:
        parametros = dados['parametros']
        dict_dir = dados['dict_dir']
        if parametros:
            df_parametros = pd.DataFrame(
                parametros
            ).T
            st.header('Tabela com os parametros URL')
            st.dataframe(df_parametros)
        else:
            st.info("Não há parametros na URL passada!")
        st.divider()
        st.header('Localização da página nos diretórios')
        st.json(dict_dir)
        
        st.subheader(f'Quer analisar o sitemap do {dict_dir["DIRETORIO_1"]}?')
        botao_analisar_sitemap = st.button(
            'Analisar SITEMAP',
            on_click=analisar_sitemap)
        st.info('Esse analisador foi feito para analisar funis de vendas através do sitemap do site. Não recomendado para sites como youtube.com, github.com e google.com.')
        if st.session_state['analisar_sitemap']:
            if botao_analisar_sitemap:
                try:
                    caminho_xml = 'https://' + dict_dir["DIRETORIO_1"]+'/'
                    res_bs4 = extrair_sitemap(caminho_xml)
                    st.write(res_bs4)
                except Exception as e:
                    #'👨🏽‍💻 O site não permitiu a leitura do sitemap. Eles estão ligados! '
                    st.info(e)
                

    
