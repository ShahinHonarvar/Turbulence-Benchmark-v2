def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(pr):
        str_pr = str(pr)
        return all((is_prime(int(str_pr[i:])) and is_prime(int(str_pr[:i])) for i in range(1, len(str_pr))))
    x = numbers[100]
    left_right_truncatables = [pr for pr in range(2, x + 1) if pr not in {2, 5} and is_prime(pr) and is_truncatable_prime(pr)]
    return sorted(left_right_truncatables, reverse=True)