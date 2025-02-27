from itertools import cycle

def lists_with_product_equal_n(circular_list):
    n = 247
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(1, length + 1):
            sublist = list(circular_list[start:start + end]) if start + end <= length else [circular_list[i % length] for i in range(start, start + end)]
            if len(sublist) > 0 and all((isinstance(x, int) for x in sublist)) and all((x > 0 for x in sublist)) and (len([factor for factor in sublist if n % factor == 0]) == len(sublist)) and (abs(int(''.join(map(str, sublist))) - n) % n == 0):
                result.append(sublist)
    return result