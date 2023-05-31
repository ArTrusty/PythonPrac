import random
import itertools
deck = list(itertools.product(['king','queen','jack','ace', '2','3','4','5','6','7','8','9','10'], ['hearts','diamonds','clubs','spades']))
random.shuffle(deck)
for i in range(5):
    
    
    print(deck[i][0],deck[i][1])
