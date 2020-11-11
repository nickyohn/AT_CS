# UK Currency Homework

target = 200  # pence
coins = [1,2,5,10,20,50,100]  # in pence
combos = [0]*(target+1)

for coin in coins:
    for i in range(target+1):
        if coin == i:
            combos[i]+=1
        if i-coin > 0:
            combos[i]=((combos)[i]+combos[i-coin])

print(combos)
print(combos[target])