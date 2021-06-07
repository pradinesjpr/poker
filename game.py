from players import Player
from cards import StandardDeck
import itertools
#from poker import *
from collections import Counter, defaultdict




class Game(object):

    


    def __init__(self):
    
        self.state = ['Pre-Flop', 'River', 'Turn']
        self.board = []
        self.player = Player()
        self.deck = StandardDeck()
        


    def dealerDeal(self):
        self.board.append(self.deck.pop(0))
        


    
        


    def changeOfState(self):

        if(self.state[0] == 'Pre-Flop'):
            self.dealerDeal()
            self.dealerDeal()
            self.dealerDeal()
            
        elif(self.state[0] == 'River'):
            
            self.dealerDeal()
            
        elif(self.state[0] == 'Turn'):
            
            self.dealerDeal()
        
        self.state.append(self.state.pop(0))

        
        


    def hand_scorer(self, player):
        
        all_cards = player.hand + self.board
        all_hand_combinations = list(itertools.combinations(all_cards, 5))

        

        for i in all_hand_combinations:

            
            
            
            for bubble_sort in range(25):
                for j in range(5):

                    a = j + 1

                    if(j == 4):
                        break
                    
                    if(i[j].value > i[a].value):
                        #print("Entrou no if, portanto ",i[j].value, "é maior que ", i[a].value)
                        aux = i[j].value
                        aux_suit = i[j].suit

                        i[j].value = i[a].value
                        i[j].suit = i[a].suit
                        i[a].value = aux
                        i[a].suit = aux_suit
                        

            
            value_list = []
            suit_list = []
            actual_hand = 0
            best_hand_values = []
            best_hand_suits = []
            best_hand = 0
            best_hand_tb = 0
            for j in i:
                suit_list.append(j.suit)
                value_list.append(j.value)

            

            if len(value_list) != 5:
                print("error")
                print(value_list)
                break
            if len(suit_list) != 5:
                print("error")
                print(suit_list)
                break

            for test in value_list:
                if test < 0:
                    print("existe um valor menor que 0 na value list")
                    break
                if test > 12:
                    print("existe um valor maior que 12 na value list")
                    break

            for test in suit_list:
                if test < 0:
                    print("existe um valor menor que 0 na suit list")
                    break
                if test > 3:
                    print("existe um valor maior que 12 na suit list")
                    break

            def check_fourkind(value_list):
                value_counts = defaultdict(lambda:0)
                for value in value_list:
                    value_counts[value] += 1
                if sorted(value_counts.values()) == [1,4]:
                    return True
                return False
            
            def check_fullhouse(value_list):
                
                value_counts = defaultdict(lambda:0)
                for value in value_list:
                    value_counts[value] += 1
                if sorted(value_counts.values()) == [2,3]:
                    
                    
                    return True
                return False
            


            def check_flush(suit_list):
                value_counts = defaultdict(lambda:0)
                for value in suit_list:
                    value_counts[value] += 1
                
                

                if sorted(value_counts.values()) == [5]:
                    
                    return True
                    
                else:
                 
                    return False

            def check_straight(value_list):
                value_counts = defaultdict(lambda:0)
                for values in value_list:
                    value_counts[values] += 1
                #rank_values = [card_order_dict[i] for i in value_list]
                value_range = max(value_list) - min(value_list)
                if sorted(value_counts.values()) == [1,1,1,1,1] and (value_range == 4):
                
                    return True
                    
                else:
                    
                    if set(value_list) == {12,0,1,2,3}:
                        
                        return True

                return False
                    

                    

            def check_threeofkind(value_list):
                value_counts = defaultdict(lambda:0)
                for value in value_list:
                    value_counts[value]+=1

                if sorted(value_counts.values()) == [1,1,3]:
                
                    return True
                else:
                    return False

            def check_doispares(value_list):
                value_counts = defaultdict(lambda:0)
                for value in value_list:
                    value_counts[value]+=1
                if sorted(value_counts.values()) == [1,2,2]:

                    return True
                else:
                    return False


            
            def check_pair(value_list):
                value_counts = defaultdict(lambda:0)
                for value in value_list:
                    value_counts[value]+=1
                if sorted(value_counts.values()) == [1,1,1,2]:
                    
                    return True
                else:

                    return False




            def check_combo(value_list,suit_list):


                

                if check_flush(suit_list) & check_straight(value_list):
                    #print("Straight Flush", value_list, suit_list)
                    return 9
                    
                        
                elif check_fourkind(value_list):
                    #print("Quadra", value_list, suit_list)
                    return 8

                elif check_fullhouse(value_list):
                    #print("Full house", value_list, suit_list)
                    return 7
                    

                elif check_flush(suit_list):
                    #print("Flush", value_list, suit_list)
                    return 6
                    
                
                elif check_straight(value_list):
                    #print("Straight", value_list, suit_list)
                    return 5
                    

                elif check_threeofkind(value_list):
                    #print("Trinca", value_list, suit_list)
                    return 4
                    

                elif check_doispares(value_list):
                    #print("Dois Pares", value_list, suit_list)
                    return 3
                    

                elif check_pair(value_list):
                    #print("Par", value_list, suit_list)
                    return 2
                    
                
                
                    
                #print("High Card", value_list, suit_list)
                return 1

            
            actual_hand = check_combo(value_list, suit_list)
            #print(actual_hand)

            
            

            if actual_hand < 1:
                print("error")
            if actual_hand > 9:
                print("error")
            
            if actual_hand > best_hand:
                best_hand = actual_hand
                best_hand_tb = max(value_list)
                best_hand_values = value_list
                best_hand_suits = suit_list
            
            if actual_hand == best_hand:
                if max(value_list) > best_hand_tb:
                    best_hand_tb = max(value_list)
                    best_hand_values = value_list
                    best_hand_suits = suit_list

            

            
            
          

        
            
       

        return best_hand
        
        
                 
                    
            
            

               
                
    



            

            




