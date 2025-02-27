def sum_ints_div_by_either_nums(numbers):
    divisor = {-553, -737}
    return sum((num for i, num in enumerate(numbers[543:585]) if any((num % div == 0 for div in divisor))))