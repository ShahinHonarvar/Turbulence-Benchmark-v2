def all_right_truncatable_prime(numbers):
    x = numbers[61]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(len(str(i)) - 1, 0, -1):
            truncated_num = int(str(i)[:j])
            if not is_prime(truncated_num):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True