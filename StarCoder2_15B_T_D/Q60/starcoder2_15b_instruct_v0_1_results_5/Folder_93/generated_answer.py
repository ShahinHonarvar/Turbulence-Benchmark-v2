def all_left_right_truncatable_prime(t):
    x = t[11]
    prime_list = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_prime_list = [i for i in prime_list if is_left_right_truncatable(i, prime_list)]
    return sorted(truncatable_prime_list)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n, prime_list):
    s = str(n)
    for i in range(len(s)):
        if int(s[i:]) not in prime_list or int(s[:i + 1]) not in prime_list:
            return False
    return True