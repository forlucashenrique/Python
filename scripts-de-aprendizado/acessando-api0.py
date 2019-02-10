"""
    Sou iniciante na programação e estou adorando esse mundo! Esse desafio foi proposto no curso
    Web Morderno do Professor Leonardo Mourão junto com a Cod3r.

    É minha primeira vez acessando uma API(se é que eu posso chamar assim, ainda não entendo sobre API'S).
    # O desafio é simples: acessar a URL onde está um arquivo JSON e encontrar a mulher chinesa com 
    o menor salário.

"""

import requests, json
from pprint import pprint

class Array(list):

    """
        Tentativa de representar o tipo de dado Array do Javascript. Mais precisamente, a classe
        simula a implementação dos métodos 'FILTER' e 'REDUCE'.

        Tipo Array: herda do tipo LIST e implementa mais dois metódos.
    """

    def __init__(self, iterable):
        super().__init__(iterable)

    def filter(self, callback):
        
        novo_array = Array([])

        for obj in self:
            if callback(obj):
                novo_array.append(obj)
    
        return novo_array

    def reduce(self, callback):
        acumulador = self[0]

        for elemento in self:
            acumulador = callback(acumulador, elemento)

        return acumulador

    def map(self, callback):
        """
            Também é um metódo do Javascript. A implementação é para fins didáticos e não é usado 
            neste exercício.
        """

        novo_array = Array([])

        for elemento in self:
            novo_array.append(callback(elemento))
        
        return novo_array
    
        
class Service:
    
    def __init__(self):
        self.url = 'http://files.cod3r.com.br/curso-js/funcionarios.json'
        self._funcionarios = []

    @property
    def funcionarios(self):
        self._funcionarios = requests.get(self.url)
        self._funcionarios = json.loads(self._funcionarios.content)
        self._funcionarios = Array(self._funcionarios)
        return self._funcionarios


def pegar_chineses(funcionario):
    return funcionario['pais'] == 'China'


def pegar_mulheres(funcionario):
    return funcionario['genero'] == 'F'


def pegar_menor_salario(a, b):

    if a['salario'] < b['salario']:
        return a 
    else:
        return b 


if __name__ == '__main__':

    serviço = Service()
    funcionarios = serviço.funcionarios
    chineses = funcionarios.filter(pegar_chineses)
    mulheres = chineses.filter(pegar_mulheres)
    mulher_com_menor_salario = mulheres.reduce(pegar_menor_salario)

    pprint(mulher_com_menor_salario)



