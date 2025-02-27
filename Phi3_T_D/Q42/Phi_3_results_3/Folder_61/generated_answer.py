from math import sqrt

def prime_factors(int_list):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of(num):
        factors = set()
        i = 2
        while i <= num:
            if num % i == 0 and is_prime(i):
                factors.add(i)
                num //= i
            else:
                i += 1
        return factors
    try:
        index_eight_num = int_list[8]
        return prime_factors_of(index_eight_num)
    except IndexError:
        return "There's no element at index 8 in the provided list."