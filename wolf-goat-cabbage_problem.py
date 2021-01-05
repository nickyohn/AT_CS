# list of characters (all start on west bank)
list = ['man', 'goat', 'wolf', 'cabbage']
path = []

# defines who can eat who
def eats(x, y):
    # goat eats cabbage
    if x == 'goat' and y == 'cabbage':
        return True
    # wolf eats cabbage
    elif x == 'wolf' and y == 'goat':
        return True
    else:
        return False

# defines pair of characters who can safely cross the river
def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True

# returns state of each character
def state_of(character, state):
    try:
        return state[character]

# returns true/false for different safe states
def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('wolf', state):
        return False
    elif state_of('goat', state) == state_of('cabbage', state):
        return False
    else:
        return True
