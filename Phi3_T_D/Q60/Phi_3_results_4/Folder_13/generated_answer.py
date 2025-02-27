def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    truncatable_prime_list = []
    for n in range(23, x + 1):
        temp = str(n)
        if all((is_prime(int(temp[i:])) and is_prime(int(temp[:len(temp) - i])) for i in range(len(temp)))):
            truncatable_prime_list.append(int(temp))
    return truncatable_prime_list