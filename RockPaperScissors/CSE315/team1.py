'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
import random

strategy_name = 'Beat their last move if NOT repeating'

def beat_move(move): # I changed move function as requested
    if move=='r':
        return 's'
    if move == 'p':
        return 'r'
    if move=='s':
        return 'p'

def move(my_history, their_history):
    '''This player always starts with rock
    '''
    if len(their_history)<3:
        return 'p'          # I changed it so they always start with paper
    if their_history[-1]!=their_history[-2]: # I changed this so it would... 
        return beat_move(their_history[-1])#...beat last move if not repeating
    return random.choice(['r','p','s'])
    