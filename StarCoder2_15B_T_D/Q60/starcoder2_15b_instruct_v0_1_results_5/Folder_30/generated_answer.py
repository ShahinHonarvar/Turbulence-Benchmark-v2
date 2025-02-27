def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[37]
    is_truncatable_prime = lambda n: all((int(str(n)[i:]) in prime_set for i in range(len(str(n))))) and all((int(str(n)[:i + 1]) in prime_set for i in range(len(str(n)))))
    prime_set = set((i for i in range(2, x + 1) if all((i % j for j in range(2, int(i ** 0.5) + 1)))))
    return sorted(filter(is_truncatable_prime, prime_set), reverse=True)