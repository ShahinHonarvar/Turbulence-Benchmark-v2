def all_right_truncatable_prime(numbers):
    x = numbers[758]
    return [i for i in range(2, x) if right_truncatable_prime(i)]