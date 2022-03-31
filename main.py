# importar app, importar builder(gui)
# criar apk
# criar a build
from kivy.app import App
from kivy.lang import Builder
import  requests

GUI = Builder.load_file("tela.kv")


class Prototipo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = self.pegar_cotacao("USD")

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


Prototipo().run()
