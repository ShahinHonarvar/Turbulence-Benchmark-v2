def all_left_truncatable_prime(input_tuple: tuple) -> list:
    x = input_tuple[19]
    prime_numbers = []
    is_prime = [True] * x
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    for i in range(2, x):
        if is_prime[i]:
            truncatable = True
            temp = i
            while temp > 9:
                temp //= 10
                if not is_prime[temp]:
                    truncatable = False
                    break
            if truncatable:
                prime_numbers.append(i)
    prime_numbers.sort()
    return prime_numbers