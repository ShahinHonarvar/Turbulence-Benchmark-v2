def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[543:585]) if num % -553 == 0 or num % -737 == 0))