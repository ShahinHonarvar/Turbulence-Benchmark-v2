def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if number > 0:
            number_str = str(number)
            if '0' not in number_str:
                is_left_right_truncatable_prime = True
                for i in range(1, len(number_str)):
                    if int(number_str[i:]) % 2 == 0 or int(number_str[:i]) % 2 == 0:
                        is_left_right_truncatable_prime = False
                        break
                if is_left_right_truncatable_prime:
                    left_right_truncatable_primes.append(number)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes