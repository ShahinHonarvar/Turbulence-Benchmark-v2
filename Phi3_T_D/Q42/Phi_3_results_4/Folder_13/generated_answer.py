from collections import Counter
import math

def prime_factors(numbers):
    prime_factors_set = set()
    num = numbers[126]
    while num % 2 == 0:
        prime_factors_set.add(2)
        num = num // 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            prime_factors_set.add(i)
            num = num // i
    if num > 2:
        prime_factors_set.add(num)
    return prime_factors_set