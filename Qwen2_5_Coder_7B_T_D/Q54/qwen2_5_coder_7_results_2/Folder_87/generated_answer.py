def all_right_truncatable_prime(numbers):
    x = numbers[39]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        if all((int(str(num)[::-1][:i + 1]) % 2 != 0 and int(str(num)[::-1][:i + 1]) % 3 != 0 and (int(str(num)[::-1][:i + 1]) % 5 != 0) and (int(str(num)[::-1][:i + 1]) % 7 != 0) for i in range(len(str(num)[::-1])))):
            primes.append(num)
    return sorted([p for p in primes if all_right_truncatable(p)], reverse=True)

def all_right_truncatable(num):
    for i in range(len(str(num))):
        if int(str(num)[::-1][:i + 1]) not in primes:
            return False
    return True