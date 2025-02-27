def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    output_list = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(prime)) - 1):
            truncated_prime = int(str(prime)[i + 1:])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
            truncated_prime = int(str(prime)[:-i - 1])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
        if is_truncatable:
            output_list.append(prime)
    output_list.sort(reverse=True)
    return output_list

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True