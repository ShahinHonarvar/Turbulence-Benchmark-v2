from typing import List

def all_left_truncatable_prime(input_tuple: tuple) -> List[int]:
    """
    Finds all left-truncatable prime numbers less than the integer at index 767 of the input tuple.
    """
    x = input_tuple[767]
    output_list = []

    def is_left_truncatable_prime(num: int) -> bool:
        if num < 10:
            return num in (2, 3, 5, 7)
        return is_left_truncatable_prime(num // 10) and is_prime(num)

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(x):
        if is_left_truncatable_prime(i):
            output_list.append(i)
    return sorted(output_list, reverse=True)