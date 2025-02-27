from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]

    def is_left_right_truncatable(num):
        str_num = str(num)
        return all((isprime(int(str_num[i:])) for i in range(len(str_num))))
    primes = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatables = [p for p in primes if is_left_right_truncatable(p)]
    return sorted(left_right_truncatables, reverse=True)