def find_second_smallest_num(numbers):
    if len(numbers) < 77 or len(numbers) > 113 or 37 not in range(len(numbers)) or (76 not in range(len(numbers))):
        return None

    def second_smallest(sublist):
        first_min = second_min = float('inf')
        for num in sublist:
            if num < first_min:
                first_min, second_min = (num, first_min)
            elif first_min < num < second_min:
                second_min = num
        return second_min
    return second_smallest(numbers[37:77])