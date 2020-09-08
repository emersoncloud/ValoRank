from random import shuffle

# Things I want to add
# Ability to set parts of teams


class Player:
  def __init__(self, name, rank):
    self.name = name
    self.rank = rank
  
  def __repr__(self):
    return repr((self.name, self.rank))

class Team:
  def __init__(self):
    self.players = {}
    self.totalSkill = 0

  def addPlayer(self, player):
    self.players[player.name] = player
    self.totalSkill += player.rank

  def removePlayer(self, player):
    if self.players.get(player) is not None:
      deletedPlayer = self.players.pop(player)
      self.totalSkill -= deletedPlayer.rank

  def getSkill(self):
    return self.totalSkill

  def printer(self):
    print("Total Rank: ", self.totalSkill)
    for name, value in self.players.items():
      print(f"{value.rank}\t-{value.name}")

  def clear(self):
    self.players = {} 
    self.totalSkill = 0

  def __repr__(self):
    return repr((self.players, self.totalSkill))


    
def printList(list):
  for player in list:
    print(player)

# playerList = [
#   Player("firinn", 13),
#   Player("memerson", 7),
#   Player("prime8", 6),
#   Player("Prapor", 7),
#   Player("Steven", 7),
#   Player("ManMythMariner", 4),
#   Player("Selsskorr", 11),
#   Player("jeprunner", 2),
#   Player("smashdj", 7),
#   Player("Sven The Surfer", 9)
# ]

# iron 1
# bronze 2
# silver 3
# gold 4
# plat 5


playerList = [
  Player("firinn", 4),
  Player("LordoTheRings", 4),
  Player("memerson", 3),
  Player("prime8", 3),
  # Player("Selsskorr", 4),
  Player("ManMythMariner", 1),
  # Player("whiteboy", 3),
  # Player("whiteguy", 2),
  Player("mistake", 2),
  Player("happynoose", 2),
  Player("Prapor", 3),
  # Player("jeprunner", 1),
  # Player("sven", 3),
  Player("goombis", 3),
  Player("Kory", 3)
]


team1 = Team()
team2 = Team()

playerListRandom = shuffle(playerList)
printList(playerList)
print("\n")

difference = 100
while (difference > 1):
  team1.clear()
  team2.clear()
  for x in range(0,int(len(playerList)/2)):
    team1.addPlayer(playerList[x])

  for x in range(int(len(playerList)/2), int(len(playerList))):
    team2.addPlayer(playerList[x])

  shuffle(playerList)
  difference = abs(team1.getSkill() - team2.getSkill())


print("Team 1")
team1.printer()
print("\n")
print("Team 2")
team2.printer()