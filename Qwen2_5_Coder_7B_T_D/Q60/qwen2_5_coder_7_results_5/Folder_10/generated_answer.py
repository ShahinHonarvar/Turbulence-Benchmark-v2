def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((int(digit) != 0 and int(digit) % 2 != 0 for digit in str(num))):
            is_prime = True
            for i in range(len(str(num))):
                if int(str(num)[i:]) not in primes:
                    is_prime = False
                    break
                if int(str(num)[:i + 1]) not in primes:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes, reverse=True)