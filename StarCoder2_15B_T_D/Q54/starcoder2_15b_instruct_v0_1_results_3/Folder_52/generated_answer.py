def all_right_truncatable_prime(input_tuple):
    x = input_tuple[52]
    prime_numbers = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    right_truncatable_prime_numbers = []
    for prime_number in prime_numbers:
        right_truncatable = True
        truncated_number = prime_number
        while truncated_number > 0:
            if not is_prime_number(truncated_number):
                right_truncatable = False
                break
            truncated_number //= 10
        if right_truncatable:
            right_truncatable_prime_numbers.append(prime_number)
    right_truncatable_prime_numbers.sort(reverse=True)
    return right_truncatable_prime_numbers

def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True