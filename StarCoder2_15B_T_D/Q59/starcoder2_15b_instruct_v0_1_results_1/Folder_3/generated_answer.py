import math

def all_left_truncatable_prime(numbers):
    """
    Returns a list of all left-truncatable prime numbers less than the integer at index 100.
    """
    x = numbers[100]
    result = []
    for num in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not math.isprime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(num)
    return sorted(result)