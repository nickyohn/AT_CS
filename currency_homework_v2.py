# UK Currency Homework

target = 200  # pence
coins = [1,2,5,10,20,50,100]  # in pence
combos = [0]*(target+1)  # create array that shows total number of combos that can be made up to that coin (starting from lowest) 
				
for coin in coins:
    for i in range(target+1): 
        if coin == i:
            combos[i]+=1  # if coin is less than/equal to target sum, it can be used at least once
        if i-coin > 0:
            combos[i]=((combos)[i]+combos[i-coin]) # number of combos accumulates as we iterate through coins

print(combos)	# print entire array
print("number of possible ways to make 2 pounds: ", combos[target])	  # print last index (total number of combos)