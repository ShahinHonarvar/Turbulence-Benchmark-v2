def all_left_truncatable_prime(x):
    is_prime = [True] * x
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    prime_nums = [i for i in range(x) if is_prime[i]]
    left_truncatable_prime = [num for num in prime_nums if all((int(str(num)[i]) in prime_nums for i in range(1, len(str(num)))))]
    left_truncatable_prime.sort()
    return left_truncatable_prime