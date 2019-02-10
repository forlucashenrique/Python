import requests, json

class HGapi:

    def __init__(self, param, key):
        """
            Inicaliza a consulta à api da HG Brasil.

            parâmetros => param: finance, weather | key: 'chave criada no site da HG Brasil'   
        """
        self.url = f'https://api.hgbrasil.com/{param}?format=debug&key={key}'
        self._json_dados = requests.get(self.url)
        self.status_code = self._json_dados.status_code

    @property
    def dolar(self):
        dict_dados = json.loads(self._json_dados.content)
        return f"USD: {dict_dados['results']['currencies']['USD']['buy']}"


if __name__ == '__main__': 
    finance = HGapi('finance', 'key')
    print(finance.dolar)


