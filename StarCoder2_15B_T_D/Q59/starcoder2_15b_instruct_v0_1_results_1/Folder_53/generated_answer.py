import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[86]
    result = []
    for i in range(1, len(str(x)) + 1):
        for permutation in itertools.permutations(str(x), i):
            number = int(''.join(permutation))
            if is_prime(number):
                result.append(number)
    result.sort(reverse=True)
    return result