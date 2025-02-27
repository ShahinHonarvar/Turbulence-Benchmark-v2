def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[52]
    truncatables = []
    p = [i for i in range(2, x) if str(i).startswith('2') and is_prime(i)]
    for prime in sorted(p, reverse=True):
        s = str(prime)
        added = False
        while len(s) > 1:
            s = s[1:]
            if is_prime(int(s)) and s not in truncatables:
                truncatables.append(int(s))
                added = True
        if added and len(str(prime)) > 1:
            truncatables.append(prime)
    return sorted(truncatables, reverse=True)