def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    primes = [2, 3, 5, 7]
    if x < 11:
        return []
    for num in range(11, x + 1):
        if all((int(str(num)[:i]) % 2 != 0 and int(str(num)[:i]) % 3 != 0 and (int(str(num)[:i]) % 5 != 0) and (int(str(num)[:i]) % 7 != 0) for i in range(1, len(str(num))))) and all((int(str(num)[-i:]) % 2 != 0 and int(str(num)[-i:]) % 3 != 0 and (int(str(num)[-i:]) % 5 != 0) and (int(str(num)[-i:]) % 7 != 0) for i in range(1, len(str(num))))) and all((int(digit) != 0 for digit in str(num))) and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes)