dollar = float(input("Enter Amount: "))
while dollar < 0:
    dollar = float(input("Enter a positive Number: "))
    
cents = round(dollar * 100)
coins = 0
#quarters
while cents >= 25:
    coins += 1
    cents = cents - 25
    
# Dimes
while cents >= 10:
    coins += 1
    cents = cents - 10
    
#Nickels
while cents >= 5:
    coins += 1
    cents = cents - 5
    
#Pennies
while cents >= 1:
    coins += 1
    cents = cents - 1
    
print(f"Number of coins {coins}")
