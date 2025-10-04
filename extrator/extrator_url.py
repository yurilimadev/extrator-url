import re
from urllib.parse import urlparse, parse_qs


def sanitiza_url(url):
    if type(url) == str:
        return url.strip()
    else:
        return ""


class ExtratorURL:

    def __init__(self, url):
        self.url = sanitiza_url(url)
        self.valida_lista()

    def valida_lista(self):
        padrao = re.compile(r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
        match = padrao.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def valida_url(self):
        if not self.url:
            raise ValueError('URL esta vazia!')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_diretorio_json(self):
        lista = self.get_url_base().split('/')
        lista.remove('')
        json_dir = {}
        for i, dir_ in enumerate(lista):
            if i == 0:
                json_dir['SERVIÇO'] = lista[i].replace(':','')
            if i >= 1:
                json_dir[f'DIRETORIO_{i}'] = lista[i]
        return json_dir

    def get_url_parametros(self):
        url_analisada = urlparse(self.url)
        parametros = parse_qs(url_analisada.query)
        
        
        #tratando saida
        parametros_validos = {
            key: value for key, value in parametros.items() if value
        }
        return parametros

    

if __name__ == '__main__':
    url = 'https://www.sympla.com.br/evento-online/bibliometria-com-bibliometrix-e-biblioshiny-com-o-software-r-teoria-e-pratica/3091409?utm_medium=paid&utm_source=ig&utm_id=120230730305190318&utm_content=120230730305660318&utm_term=120230730305300318&utm_campaign=120230730305190318&fbclid=PAb21jcAM9L-BleHRuA2FlbQEwAGFkaWQBqyU2VXyXHgGnVF4WSSyd1aUKH6Uj5cyp5G82ujhYmIHFZil4Nm3LZ8CqlEr3RIU-1yYg48U_aem_PpSJHf-PRKrgAS8wxYV9vQ&referrer=instagram.com'
    classe_url = ExtratorURL(url)
    print("URL BASE")
    print(classe_url.get_url_base())
    print("URL PARAMETROS")
    print(classe_url.get_url_parametros())
    print("URL JSON")
    print(classe_url.get_diretorio_json())