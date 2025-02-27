def find_second_smallest_num(numbers):
    smallest = float('inf')
    second_smallest = float('inf')
    for n in numbers[:5]:
        if n < smallest:
            second_smallest, smallest = (smallest, n)
        elif smallest < n < second_smallest:
            second_smallest = n
    return second_smallest if second_smallest != float('inf') else None