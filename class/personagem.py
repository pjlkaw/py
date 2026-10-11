class Personagem:
    def __init__(self, id):
        self.nome = f"Player{id}"
        self.vida = 100

    def recebeDano(self, dano):
        self.vida = self.vida - dano

players = []

for i in range(1, 4):
    idPlayer = i
    player = Personagem(idPlayer)
    players.append(player)
    print(player.nome)

for player in players:
    player.recebeDano(10)
    print(player.nome, " - ", player.vida)
