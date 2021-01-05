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
