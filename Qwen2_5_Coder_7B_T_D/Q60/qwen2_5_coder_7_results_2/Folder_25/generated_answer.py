def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if all((int(digit) % 2 != 0 and int(digit) != 5 for digit in str(num))):
            for i in range(len(str(num))):
                if int(str(num)[i:]) not in primes:
                    break
            else:
                for i in range(len(str(num)) - 1, 0, -1):
                    if int(str(num)[:i]) not in primes:
                        break
                else:
                    primes.append(num)
    return sorted(primes)