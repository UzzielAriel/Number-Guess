import time, datetime, random
from colorama import Fore

class guess:
  def __init__(self, ai):
    if ai == True:
      self.aiguess()
    self.aoguesses = 0
    self.guesses = []
  def aiguess(self):
    self.getrandom()
    self.i = 0
    while True:
      self.i += 1
      if self.i == self.randomint:
        print("The correct number is: " + str(self.i) + " guessed by AI")
        break
  def getrandom(self):
    random.seed(datetime.datetime.now().strftime("%f"))
    self.randomint = random.randint(1,1000)
  def getguess(self):
    print("Your guesses: " + str(self.aoguesses))
    if self.aoguesses > 0:
      print("Your recent guesses: "+ " ".join(self.guesses))
    print("Guess a number from 1 - 1000")
    self.guess = input()
    self.check()
  def check(self):
    if self.guess.isdigit() == False:
      print("Your guess has to be a number")
      time.sleep(2)
      self.getguess()
    if int(self.guess) > self.randomint:
      print("The number is lower")
      self.guess += "(h)"
      self.guesses.append(Fore.RED + self.guess + Fore.WHITE)
      self.aoguesses += 1
      time.sleep(2)

      self.getguess()
    elif int(self.guess) < self.randomint:
      print("The number is higher")
      self.guess += "(l)"
      self.guesses.append(Fore.GREEN + self.guess + Fore.WHITE)
      self.aoguesses += 1
      time.sleep(2)

      self.getguess()
    elif int(self.guess) == self.randomint:
      print("You guessed correct!")
      self.aoguesses = 0
      self.guesses = []
      self.guess = ""
      time.sleep(2)
      self.getrandom()
      self.getguess()

object2 = guess(True)
print("Your  turn: ")
object = guess(False)
object.getrandom()
object.getguess()