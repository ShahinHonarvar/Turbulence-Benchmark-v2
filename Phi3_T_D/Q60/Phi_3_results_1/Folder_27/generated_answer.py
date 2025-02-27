def all_left_right_truncatable_prime(tpl):
    primes = [str(n) for n in tpl]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num_str):
        return all([is_prime(int(num_str[i:])) and is_prime(int(num_str[:i + 1])) for i in range(len(num_str)) if i > 0 and i < len(num_str) - 1])
    x = int(primes[78])
    return sorted([int(p) for p in primes if is_prime(int(p)) and is_truncatable(p) and (int(p) <= x)], reverse=True)