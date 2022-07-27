coin25 = 0
coin10 = 0
coin5 = 0
coin1 = 0

while True:
    cash = float(input("Insira seu troco: "))
    if cash <= 0:
        continue
    else:
        break

cents = round(cash * 100)

while (cents > 25 or cents == 25):
    cents = cents - 25
    coin25 += 1

while (cents > 10 or cents == 10):
    cents = cents - 10
    coin10 += 1

while (cents > 5 or cents == 5):
    cents = cents - 5
    coin5 += 1

while (cents > 1 or cents == 1):
    cents = cents - 1
    coin1 += 1

print(f"coins of 25 cents: {coin25}")
print(f"coins of 10 cents: {coin10}")
print(f"coins of 5 cents: {coin5}")
print(f"coins of 1 cents: {coin1}")
print(f"necessary coins: {coin25 + coin10 + coin5 + coin1}")