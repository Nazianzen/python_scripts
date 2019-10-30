# Fizzbuzz prints 'fizz' for multiples of 3,
# 'buzz' for multiples of 5
# and 'fizzbuzz' for multiples of both

for num in range(0, 50):
    if num % 3 == 0 and num % 5 == 0 and num != 0:
        print('fizzbuzz')
    elif num % 3 == 0 and num != 0:
        print('fizz')
    elif num % 5 == 0 and num != 0:
        print('buzz')
    else:
        print(num)
