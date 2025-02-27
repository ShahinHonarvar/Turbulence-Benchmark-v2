def all_right_truncatable_prime(numbers):
    """
    Creates a sorted list of all right-truncatable prime numbers less than x, where x is the 36th element of the input tuple.
    """
    x = numbers[35]
    right_truncatable_prime = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            number_str = str(i)
            for k in range(len(number_str) - 1, 0, -1):
                truncated_number = int(number_str[:k])
                if not is_prime_number(truncated_number):
                    is_prime = False
                    break
        if is_prime:
            right_truncatable_prime.append(i)
    right_truncatable_prime.sort(reverse=True)
    return right_truncatable_prime

def is_prime_number(number):
    """
    Checks if a number is a prime number.
    """
    for i in range(2, number):
        if number % i == 0:
            return False
    return True