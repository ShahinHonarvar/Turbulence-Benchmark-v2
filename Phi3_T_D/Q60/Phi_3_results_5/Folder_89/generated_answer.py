def all_left_right_truncatable_prime(numbers):
    smallest_two_digit_prime = 11
    is_prime = [False, False] + [True] * (numbers(97) - 1)
    for i in range(2, int(numbers(97) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, numbers(97) + 1, i):
                is_prime[j] = False

    def is_truncatable_prime(n):
        s = str(n)
        return all((is_prime[int(s[i:])] for i in range(len(s))))
    results = [n for n in range(smallest_two_digit_prime, numbers(97) + 1) if is_prime[n] and is_truncatable_prime(n)]
    return sorted(results, reverse=True)