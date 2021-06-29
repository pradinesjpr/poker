from collections import defaultdict
from cards import StandardDeck
from players import Player
import itertools
from game import Game


montecarlo_iterations = 0

result = defaultdict(lambda:0)

while montecarlo_iterations < 30000:
    
    game = Game()

    game.deck.shuffle()

    game.deck.deal(game.player)

    game.deck.deal(game.player)
 
    

    game.changeOfState()

    game.changeOfState()

    game.changeOfState()


    scores = game.hand_scorer(game.player)
    
    
    result[scores] += 1
    
    montecarlo_iterations += 1



print(sorted(result.items()), montecarlo_iterations)


