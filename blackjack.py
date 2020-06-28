# embaralhar cartas
import random

playing = False
chip_pool = 100

bet = 1
restart_phrase = "press 'd' to shuffle again por press 'q' to leave."

suits = ('H','D','C','S')
ranking = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
card_val ={'A':2,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}


#criar as cartas

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank
    
    def grab_suit(self):
        return self.suit
    
    def grab_rank (self):
        return self.rank
    
    def draw(self):
        return print(self.suit + self.rank)

#criando e Mostrando sua mão

class Hand:
    def __init__(self):
        self.cards =[]
        self.value = 0
        self.ace = False
    def __str__(self):
        hand_comp = ''

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name
        return "Tua mão has{}".format(1== hand_comp)
    
    def card_add(self,card):
        
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
            
        self.value += card_val[card.rank]

    #função para tratar o Ás
        
    def calc_val(self):
        if(self.ace == 'True' and self.value<12):
            return self.value +10
        else:
            return self.value
    def draw (self,hidden):
        if hidden == True and playing ==True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range (starting_card,len(self.cards)):
            self.cards[x].draw()
    

#Baralho

class Deck:
    def __init__(self):
        self.deck =[]

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__ (self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +=" " + card.__str__()
        return "Deck Has" + deck_comp



#função aposta

def make_bet():
    global bet
    bet = 0

    print ("what amount of chips you would like to bet?(Enter whole interger please)")

    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print ('aposta invalida' + str(chip_pool) + " Fichas sobrando")


def deal_cards():
    global result,playing,deck,player_hand,dealer_hand, chip_pool,bet

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()
    
# duas cartas para o jogador

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

# Duas cartas para o dealer
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? press 'h' or 's':"

    chip_pool -= bet

    playing = True
    game_step()



def hit():

    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print ('A mão do jogardo is %s' %player_hand)

        if player_hand.calc_val() >= 21:
            result = "Deu ruim! " + restart_phrase
            chip_pool -=bet
            playing = False
        else:
            result = "Não tem mais como dar hit" + restart_phrase

        game_step()


def stand():

    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing == False:
        if player_hand.calc_val() >0:
            result = "sorry, you can't stand! "

    else:
        while dealer_hand.calc_val() <17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_val() > 17:
            result = "Dealer Busted! You Win!" + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = "Dealer Busted! You Win!" + restart_phrase
            playing = False

        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = "Tied up!" + restart_phrase
            playing = False

        else:
            result = "Dealer wins" + restart_phrase
            chip_pool -= bet
            playing = False

    game_step()





def game_step():
    print("")
    print('Player Hand is:')
    player_hand.draw(hidden = False)
    print ("Player hand total is:" + str(player_hand.calc_val()))

    print("")
    print('Dealer Hand is:')
    dealer_hand.draw(hidden = False)
    print ("Dealer hand total is:" + str(dealer_hand.calc_val()))

    
    if playing == False:
        print ('Chip total: ' + str(chip_pool))
    print (result)

    player_input()

def game_exit():
    print ("valeu aí por ter jogado!")
    exit()


def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print ("invalido")
        player_input()


def intro():
    statement = "Bem-vindo ao black jack, chegue mais perto do 21"
    print (statement)


deck = Deck ()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

intro()

deal_cards()

        


        
