def all_left_truncatable_prime(tup: tuple) -> list:
    x = tup[39]

    def is_left_truncatable(num: int) -> bool:
        return all((int(str(num)[i:]) in prime_nums for i in range(len(str(num)))))
    prime_nums = list(filter(is_left_truncatable, range(2, x)))
    return sorted(prime_nums, reverse=True)