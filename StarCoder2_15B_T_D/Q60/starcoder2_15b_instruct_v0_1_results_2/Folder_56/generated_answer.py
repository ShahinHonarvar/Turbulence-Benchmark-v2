def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        is_left_right_truncatable_prime = True
        number_string = str(number)
        for i in range(len(number_string)):
            left_truncatable_prime = int(number_string[i:])
            right_truncatable_prime = int(number_string[:len(number_string) - i])
            if not is_prime(left_truncatable_prime) or not is_prime(right_truncatable_prime):
                is_left_right_truncatable_prime = False
                break
        if is_left_right_truncatable_prime:
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True