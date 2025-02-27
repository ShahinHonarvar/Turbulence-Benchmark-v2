def all_right_truncatable_prime(numbers):

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

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        temp = n
        while temp:
            if not is_prime(temp):
                return False
            temp = temp // 10
        return True
    prime_list = [num for num in range(2, numbers[784]) if is_right_truncatable_prime(num)]
    return sorted(prime_list)