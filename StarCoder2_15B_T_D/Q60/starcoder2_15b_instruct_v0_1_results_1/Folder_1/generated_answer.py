def all_left_right_truncatable_prime(tup):
    x = tup[20]
    return sorted([p for p in range(2, x + 1) if all((int(str(p)[i:]) in prime_set and int(str(p)[:i]) in prime_set for i in range(2, len(str(p)))))], reverse=True)