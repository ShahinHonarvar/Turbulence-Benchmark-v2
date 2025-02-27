def all_left_right_truncatable_prime(t):
    x = t[81]
    return sorted([p for p in range(2, x + 1) if all((int(str(p)[i:]) in prime_list and int(str(p)[:i]) in prime_list for i in range(1, len(str(p)))))], reverse=True)