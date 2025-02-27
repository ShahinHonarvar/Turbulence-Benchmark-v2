def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes

def is_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    if n == 5:
        return True
    if n % 5 == 0:
        return False
    if n == 7:
        return True
    if n % 7 == 0:
        return False
    if n == 9:
        return False
    if n == 11:
        return True
    if n % 11 == 0:
        return False
    if n == 13:
        return True
    if n % 13 == 0:
        return False
    if n == 15:
        return False
    if n == 17:
        return True
    if n % 17 == 0:
        return False
    if n == 19:
        return True
    if n % 19 == 0:
        return False
    if n == 21:
        return False
    if n == 23:
        return True
    if n % 23 == 0:
        return False
    if n == 25:
        return False
    if n == 27:
        return False
    if n == 29:
        return True
    if n % 29 == 0:
        return False
    if n == 31:
        return True
    if n % 31 == 0:
        return False
    if n == 33:
        return False
    if n == 35:
        return False
    if n == 37:
        return True
    if n % 37 == 0:
        return False
    if n == 39:
        return False
    if n == 41:
        return True
    if n % 41 == 0:
        return False
    if n == 43:
        return True
    if n % 43 == 0:
        return False
    if n == 45:
        return False
    if n == 47:
        return True
    if n % 47 == 0:
        return False
    if n == 49:
        return False
    if n == 51:
        return False
    if n == 53:
        return True
    if n % 53 == 0:
        return False
    if n == 55:
        return False
    if n == 57:
        return False
    if n == 59:
        return True
    if n % 59 == 0:
        return False
    if n == 61:
        return True
    if n % 61 == 0:
        return False
    if n == 63:
        return False
    if n == 65:
        return False
    if n == 67:
        return True
    if n % 67 == 0:
        return False
    if n == 69:
        return False
    if n == 71:
        return True
    if n % 71 == 0:
        return False
    if n == 73:
        return True
    if n % 73 == 0:
        return False
    if n == 75:
        return False
    if n == 77:
        return False
    if n == 79:
        return True
    if n % 79 == 0:
        return False
    if n == 81:
        return False
    if n == 83:
        return True
    if n % 83 == 0:
        return False
    if n == 85:
        return False
    if n == 87:
        return False
    if n == 89:
        return True
    if n % 89 == 0:
        return False
    if n == 91:
        return False
    if n == 93:
        return False
    if n == 95:
        return False
    if n == 97:
        return True
    if n % 97 == 0:
        return False
    if n == 99:
        return False
    return True