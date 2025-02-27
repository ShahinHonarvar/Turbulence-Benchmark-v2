import math

def prime_factors(nums):
    num = nums[88]
    factors = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            quotient = num // i
            is_prime = True
            for j in range(2, int(math.sqrt(quotient)) + 1):
                if quotient % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.add(quotient)
    return factors