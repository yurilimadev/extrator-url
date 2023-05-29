import re


def sanitiza_url(url):
    if type(url) == str:
        return url.strip()
    else:
        return ""


class ExtratorURL:

    def __init__(self, url, lista):
        self.url = sanitiza_url(url)
        self.lista = lista
        self.valida_lista()

    def valida_lista(self, nome_site=input('Qual o nome do site? '), nome_sessao=input('Qual a sessao site? ')):
        if not self.lista:
            raise AttributeError('Lista de parametros esta vazia.')

        padrao = re.compile(f'((http)(s)?://)?(www.)?{nome_site}.com(.br)?/{nome_sessao}')
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

    def get_url_parametros(self):
        lista_paramentros = []
        pontos_ecomercial = []
        for i, letra in enumerate(self.url):
            if letra == '&':
                pontos_ecomercial.append(i)

        for i in range(len(pontos_ecomercial) + 1):
            if i < len(pontos_ecomercial):
                parametro = self.url.find(self.lista[i])
                ecomercial = pontos_ecomercial[i]
                lista_paramentros.append(self.url[parametro:ecomercial])
            else:
                parametro = self.url.find(self.lista[i])
                lista_paramentros.append(self.url[parametro:])
        return lista_paramentros


if __name__ == "__main__":
    extrator_url = ExtratorURL(url="bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar",
                               lista=['quantidade', 'moedaOrigem', 'moedaDestino'])
    print(extrator_url.get_url_parametros())
