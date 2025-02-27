import sympy

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[97]
    if x < 10:
        return []

    def is_left_truncatable(primes, number):
        if number > x:
            return False
        if number not in primes:
            return False
        if number <= 1:
            return True
        str_number = str(number)
        for i in range(1, len(str_number)):
            if sympy.isprime(int(str_number[i:])):
                continue
            else:
                return False
        return True
    result = []
    for number in range(2, x):
        if sympy.isprime(number) and is_left_truncatable({number}, number):
            result.append(number)
    return result[::-1]