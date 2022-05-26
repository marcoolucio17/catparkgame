class Cat:
  def __init__(self, inputname, inputage, inputfighttype):
    self.name = inputname
    self.age = inputage
    self.fighttype = inputfighttype
    self.friends = ["no love, only enemies"]
    self.health = 10
    self.lost = False

  def lostf(self):
      self.lostf = True
      if self.health != 0:
          self.health = 0
      print("{name} was knocked out!!".format(name = self.name))

  def lose_health(self):
      self.health -= 10
      if self.health == 0:
          self.lostf()

  def attack(self, other_cat):
      if self.lost:
          print("It lost already!!")
          return
      if self.fighttype == "CatJutsu" and other_cat.fighttype == "Boxer":
          other_cat.lose_health()
      elif self.fighttype == "Boxer" and other_cat.fighttype == "CatJutsu":
          self.lose_health()
      elif self.fighttype == "Scratcher" and other_cat.fighttype == "Boxer":
          self.lose_health()
      elif self.fighttype == "Scratcher" and other_cat.fighttype == "CatJutsu":
          other_cat.lose_health()
      elif self.fighttype == "CatJutsu" and other_cat.fighttype == "Scratcher":
          self.lose_health()
      elif self.fighttype == "Cute" and other_cat.fighttype == "CatJutsu":
          other_cat.lose_health()
      elif self.fighttype == "Cute" and other_cat.fighttype == "Boxer":
          other_cat.lose_health() 
      elif self.fighttype == "Cute" and other_cat.fighttype == "Scratcher":
          other_cat.lose_health() 
      else:
          print("Invalid fight type, try again")  
       
class Owner:
  def __init__(self, inputname1, inputcat):
    self.name = inputname1
    self.cat = inputcat
    
a = Cat("Mike", 2 , "CatJutsu")
b = Cat("Sophie", 1, "Scratcher")
c = Cat("Cleo", 8, "Boxer")
d = Cat("Meatball", 1, "Cute")

owner1 = input("Hello! What is your name?")
owner2 = input("And your opponent will be?")

choice1 = input("Player 1, please write your selection of one of this characters: Mike, Sophie or Cleo.. ")

while choice1 != "Mike" and choice1 != "Sophie" and choice1 != "Cleo" and choice1 != "Meatball":
    choice1 = input("Write a valid character, remember to write exact names")

choice2 = input("Player 2, please write your selection of one of this characters: Mike, Sophie or Cleo. If player1 already selected a character, don't use it.. ")

while choice2 == choice1 and choice2 != "Mike" and choice2 != "Sophie" and choice2 != "Cleo" and choice2 != "Meatball":
    choice2 = input("Write a valid character, remember to write exact names")



player1cat = []
player2cat = []

if choice1 == "Mike":
    player1cat.append(a)
elif choice1 == "Sophie":
    player1cat.append(b)
elif choice1 == "Cleo":
    player1cat.append(c)
elif choice1 == "Meatball":
    player1cat.append(d)
else:
    print("Something went wrong, please try again")

if choice2 == "Mike":
    player2cat.append(a)
elif choice2 == "Sophie":
    player2cat.append(b)
elif choice2 == "Cleo":
    player2cat.append(c)
elif choice1 == "Meatball":
    player2cat.append(d)
else:
    print("Something went wrong, please try again")

play1= Owner(owner1, player1cat)
play2= Owner(owner2, player2cat)

play1
play2
play1.cat[0].attack(play2.cat[0])
