from player import Player
from deck import Deck

myPlayer = Player()
myDeck = Deck()
myPlayer.currentCard = myDeck.draw()
print("Welcome to Hilo!")
print("The card is: " + str(myPlayer.currentCard))
myPlayer.guess = input("Higher or lower? [h/l]: ")
myPlayer.nextCard = myDeck.draw()
print("The next card was: " + str(myPlayer.nextCard))
answer = myPlayer.draw()
if answer:
    myPlayer.score += 100
else:
    myPlayer.score -= 75
print("Your score is: " + str(myPlayer.score))