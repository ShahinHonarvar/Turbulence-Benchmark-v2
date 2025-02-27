def all_left_right_truncatable_prime(tup):
    x = tup[54]

    def is_truncatable(num):
        s = str(num)
        if len(s) <= 2:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    truncatable_primes = [p for p in primes_list if is_truncatable(p) and p <= x]
    truncatable_primes.sort()
    return truncatable_primes