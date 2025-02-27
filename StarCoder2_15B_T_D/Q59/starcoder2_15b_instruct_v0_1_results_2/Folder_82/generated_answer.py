def all_left_truncatable_prime(x):
    return [n for n in range(2, x) if all((int(str(n)[i:]) in [2, 3, 5, 7] for i in range(len(str(n)))))]