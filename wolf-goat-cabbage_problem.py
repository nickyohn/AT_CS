# Once upon a time a farmer went to a market and purchased a wolf, a goat, and a cabbage. On his way home, the farmer came to the bank of a river and rented a boat. But crossing the river by boat, the farmer could carry only himself and a single one of his purchases: the wolf, the goat, or the cabbage.

# If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.

# The farmer's challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.

# How did he do it?

list = ['goat', 'wolf', 'cabbage']
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