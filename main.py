print("List of all prime numbers between 1 and ∞")
num = int(input("Enter a number to start with: "))
while True:
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                # print(num, "is not a prime number")
                break
        else:
            print(num)
            num+=1

    else:
        num +=1
    num+=1
