def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers, x=31):
    numbers = sorted(set(numbers), reverse=True)
    max_prime = numbers[x] if x < len(numbers) else None
    if max_prime is None:
        return []
    left_right_primes = []
    primes = [str(i) for i in range(2, max_prime + 1) if is_prime(i)]
    for num in primes:
        if len(num) < 4 or num[0] == '0' or num[-1] == '0':
            continue
        while num:
            left_trim = num[1:]
            right_trim = num[:-1]
            if int(left_trim) < max_prime and int(right_trim) < max_prime:
                left_trim_prime = left_trim and is_prime(int(left_trim))
                right_trim_prime = right_trim and is_prime(int(right_trim))
                if left_trim_prime and right_trim_prime:
                    left_right_primes.append(int(num))
            break
    return left_right_primes