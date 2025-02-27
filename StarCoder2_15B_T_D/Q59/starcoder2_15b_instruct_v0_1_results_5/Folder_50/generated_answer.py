def all_left_truncatable_prime(x):
    num = x[57]
    prime_list = [i for i in range(2, num) if all((i % j != 0 for j in range(2, i)))]
    left_truncatable_list = [prime for prime in prime_list if all((int(str(prime)[i:]) in prime_list for i in range(1, len(str(prime)))))]
    return sorted(left_truncatable_list, reverse=True)