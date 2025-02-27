import hypothetical_dataset

def prime_factors(num):
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num = num / divisor
        divisor += 1
    return factors