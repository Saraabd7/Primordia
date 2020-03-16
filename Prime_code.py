

Largest_number = 100
Lower_number = 10

print(f'Prime numbers between {Largest_number} and {Lower_number} are:: ')

for num in range(Lower_number, Largest_number + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


