def find_n_th_smallest_num(numbers):
    start, end = (18, min(82, len(numbers)))
    segment = numbers[start:end + 1]
    segment.sort()
    return segment[5]