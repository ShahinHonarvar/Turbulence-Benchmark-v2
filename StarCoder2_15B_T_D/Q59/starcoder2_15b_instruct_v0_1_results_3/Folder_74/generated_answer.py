import math

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[36]
    is_prime = [True] * x
    is_left_truncatable = [False] * x
    is_left_truncatable[2] = True
    for i in range(3, x, 2):
        if is_prime[i]:
            is_left_truncatable[i] = True
            for j in range(3, int(math.sqrt(x)) + 1, 2):
                if i % j == 0:
                    is_prime[i] = False
                    break
    result = []
    for i in range(10, x):
        if is_left_truncatable[i]:
            result.append(i)
    return sorted(result)