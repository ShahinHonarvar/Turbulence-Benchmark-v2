def all_right_truncatable_prime(numbers):
    x = numbers[97]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        number_str = str(i)
        for j in range(len(number_str) - 1, 0, -1):
            truncated_number_str = number_str[:j]
            if int(truncated_number_str) % 2 == 0 or int(truncated_number_str) % 3 == 0 or int(truncated_number_str) % 5 == 0:
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)