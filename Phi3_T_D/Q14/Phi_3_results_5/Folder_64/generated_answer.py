def find_second_smallest_num(numbers):
    count = 0
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    smallest = min(numbers[:5])
    second_smallest = None
    for num in numbers[:5]:
        if num < second_smallest:
            if num > smallest:
                second_smallest = num
                break
            else:
                count += 1
        else:
            count += 1
    return second_smallest if count > 1 else None