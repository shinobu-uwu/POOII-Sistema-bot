from bot import Bot

class BotFaustao(Bot):
    def __init__(self,nome):
        self.__nome = "Domingão do Faustão!"

    def nome(self):
        return self.__nome

    def apresentacao(self):
      return "Opa rogerinho vem cá que eu quero te contar um negócio"
 
    def mostra_comandos(self):
      return """1 - Show do faustão
2 - Churrasqueira elétrica
3 - O mundo
4 - Pegar o ovo do faustão
5 - É um país da Europa que a sua lingua é holandês
6 - SE CAPOTOU FAZ O QUE?
"""
    
    def executa_comando(self,cmd):
      if cmd == "1":
        return "Olha essa fera meu"
      if cmd == "2":
        return "Aperta 1 liga *explode*"
      if cmd == "3":
        return "O mundo é legal porque é uma bola. Se fosse duas seria um saco."
      if cmd == "4":
        return "VOCÊ ROUBOU MEU OVO!!"
      if cmd == "5":
        return "Espanha? ERROU"
      if cmd == "6":
        return "SEGURA NO BRAÇO DO XANDÃO QUE NINGUÉM MORRE."

    def boas_vindas(self):
      return "SEM PRESSÃO AQUI É XANDÃO! FALA COM O ÚLTIMO HERÓI DA TERRA"

    def despedida(self):
      return "NO FINAL DA ESCURIDÃO TEM XANDÃO. NÃO ESQUEÇA DE TRILHAR O CAMINHO DOS CAMPEÕES LADO A LADO COM SUPER XANDÃO. TUDO NOSSO!"