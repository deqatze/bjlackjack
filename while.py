import random as r
class Card:   
    deck =[]
    k=list(range(1,11))+[10,10,10]
    for i in range(4):
        deck+=k
   
class Player:
    def __init__(self):
        self.cards=[]   
        self.hit()
        self.hit()
        print(self.cards)   
    def hit(self):
        pick=Card.deck[r.randint(1,len(Card.deck)-1)]
        self.cards.append(pick)
        Card.deck.remove(pick)
    def total(self):
        self.sum=0
        if 1 in self.cards:
            i=input('1 or 11 ?  ')
            if int(i)==11:
                self.sum=sum(self.cards)+10
            else:
                self.sum=sum(self.cards)
        else:
            self.sum=sum(self.cards)
    def play(self):
        print('player cards are: ',self.cards)
        self.total()
        while self.sum<21:
            hit=input('[h]it [s]tay?  ')
        
            if hit=='h':
                self.hit()
                print('player cards are: ',self.cards)
            self.total()
            if hit=='s':
                print('player cards are: ',self.cards)
                break
    
class Game:
    def __init__(self) -> None:
        dealer=Player()
        print('dealer cards are: ',dealer.cards)
        dealer.total()
        if dealer.sum<17:
            dealer.hit()
            dealer.total()
            print('x')

        p=Player()
        p.play()


        print('dealer cards are: ',dealer.cards)
        if p.sum>21:
            print('u lose')
            return

        if p.sum>dealer.sum:
            print('u win')
        pass
a=Game()