import sys
def main():
    while True:
        n = int(input("Enter Credit Card Number: "))
        if n > 0:
            break
    
    luhn_alg(n)
    print_card(n)
   

def luhn_alg(n):
    even_sum = 0
    odd_sum = 0
    while n > 0:
        last_digit = n % 10
        odd_sum += last_digit
        even = int((n/10) % 10)
        if (2 * even) > 9:
            even = (2 * even) - 9
        else:
            even = 2 * even
        even_sum += even
        n = n//100
    sum_card = odd_sum + even_sum
    #print(f"{sum_card}")
    if sum_card % 10 == 0:
        return
    else:
        print("INVALID")
        sys.exit(0)

def print_card(n):
    if ((n >= 340000000000000 and n < 350000000000000) or (n >= 370000000000000 and n < 380000000000000)):
        print("AMEX")
    elif ((n >= 4000000000000 and n < 5000000000000) or (n >= 4000000000000000 and n < 5000000000000000)):
        print("VISA")
    elif (n >= 5100000000000000 and n <5600000000000000):
        print("MASTERCARD")
    else:
        print("INVAILD")

if __name__ =="__main__":
    main()
    
    