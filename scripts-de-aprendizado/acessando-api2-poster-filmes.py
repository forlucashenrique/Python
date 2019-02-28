#   Objetivo:  Abre um poster de um filme.
#
#   O script usa duas API'S. Uma de tradução e outra de filmes.
#
#   A API de tradução é a MyMemory: https://mymemory.translated.net/doc/spec.php. Não é completa, é uma API simples e a      #   tradução não é tão eficiente, digo isso porque as vezes o filme não é encontrado justamente pela ineficácia da tradução.
#
#   A API de filmes é a OMDb, muito simples também: http://www.omdbapi.com/
#
#  author: Lucas Henrique


import requests
import json
import webbrowser

class ApiOMDb:
    """
        OMDb é uma API de filmes. A classe busca por um filme pelo seu título em inglês.
    """

    def __init__(self, titulo_filme):
        self.apikey = '3afcdc92'
        self.url = f'http://www.omdbapi.com/?apikey={self.apikey}&t={titulo_filme}'
        self.dados = self.__req()
        self.poster = self.dados['Poster']

    def __req(self):
        try:
            req = requests.get(self.url)
        except:
            print('Erro na requisição.')
            raise SystemExit 
            
        req = json.loads(req.content)
        if req['Response'] == 'False':
            print('Filme não encontrado!')
            raise SystemExit
        return req

    def __str__(self):
        self.title = traduzir_titulo(self.dados['Title'], 'en')
        return self.title


def traduzir_titulo(titulo, idioma_de_origem):
    """
        Função que traduz o título do filme do português para o inglês e vice-versa. 
        Faz uma requisição à API MyMemory, que é uma API de Tradução simples.

        param: titulo -> título do filme em português.
        param: idioma -> idioma de origem do título. Opções: (pt-br) ou (en)

        return: título do filme traduzido para o idioma de destino. Ou Português(pt-br) ou Inglês(en)
    """
    try:
        if idioma_de_origem == 'pt-br':
            url = f'https://api.mymemory.translated.net/get?q={titulo}&langpair={idioma_de_origem}|en'
            req = requests.get(url)
        else:
            url = f'https://api.mymemory.translated.net/get?q={titulo}&type=series&langpair={idioma_de_origem}|pt-br'
            req = requests.get(url)
    except:
        raise Exception('Erro de tradução.')

    dados = json.loads(req.content)
    titulo_traduzido = dados['responseData']['translatedText']
    return titulo_traduzido


def run():
    titulo = str(input('Digite o nome do filme para ver seu POSTER: '))
    titulo_em_ingles = traduzir_titulo(titulo, idioma_de_origem='pt-br')
    filme = ApiOMDb(titulo_em_ingles)
    webbrowser.open(filme.poster)

if __name__ == '__main__':
    run()
