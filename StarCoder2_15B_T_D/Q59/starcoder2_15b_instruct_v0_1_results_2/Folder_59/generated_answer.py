def all_left_truncatable_prime(input_tuple: tuple) -> list:
    x = input_tuple[0]
    left_truncatable_prime_numbers = []
    for number in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(number))):
            truncated_number = int(str(number)[i:])
            if not is_prime(truncated_number):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_prime_numbers.append(number)
    return sorted(left_truncatable_prime_numbers, reverse=True)

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True