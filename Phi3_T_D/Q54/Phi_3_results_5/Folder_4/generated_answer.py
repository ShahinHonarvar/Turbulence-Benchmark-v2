from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[96]
    right_truncatables = []

    def is_right_truncatable_prime(n):
        return all((isprime(n) for n in str(n).rstrip('0'))) and isprime(n)
    for number in range(x - 1, 7, -1):
        if number < 10 and isprime(number):
            right_truncatables.extend(map(int, str(number)))
        elif is_right_truncatable_prime(number):
            cnt = len(str(number))
            while cnt > 1 and number % 10:
                number //= 10
                cnt -= 1
            right_truncatables.append(int(str(number)))
    return sorted(right_truncatables, reverse=True)