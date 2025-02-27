import itertools

def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, prime_set):
        if n in prime_set:
            str_n = str(n)
            for i in range(len(str_n)):
                if not is_prime(int(str_n[i:])):
                    return False
            return True
        return False
    x = numbers[67]
    prime_set = set((num for num in range(2, x) if is_prime(num)))
    result = [num for num in range(2, x) if is_left_truncatable(num, prime_set)]
    return sorted(result, reverse=True)