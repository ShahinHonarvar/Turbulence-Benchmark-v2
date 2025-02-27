def all_left_truncatable_prime(numbers):
    x = numbers[7]

    def left_truncatable_prime(x):
        if not all((int(str(x)[i:]) in prime_list for i in range(len(str(x))))):
            return False
        return True
    return sorted([i for i in prime_list if i < x and left_truncatable_prime(i)])