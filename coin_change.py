denominations = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
amount = int(input("Enter an amount of your choice: "))
count = 0
while amount != 0:
    for i in range(len(denominations)):
        if denominations[i] > amount and denominations[i - 1] < amount:
            amount -= denominations[i - 1]
            count += 1
            print("amount:{} subtracted:{}".format(amount, denominations[i - 1]))
        if denominations[i] == amount:
            amount -= denominations[i]
            count += 1
            print("amount:{} subtracted:{}".format(amount, denominations[i]))
        if denominations[-1] < amount:
            count += amount // denominations[-1]
            print("amount:{} subtracted:{}".format(amount, denominations[-1] * (amount // denominations[-1])))
            amount = amount % denominations[-1]

print(count)