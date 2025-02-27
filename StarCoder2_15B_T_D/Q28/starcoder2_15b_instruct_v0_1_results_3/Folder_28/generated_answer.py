def return_nth_smallest_ascii(string):
    count = 0
    for i, ch in enumerate(sorted(string)):
        if 25 <= i <= 77:
            count += 1
            if count == 16:
                return ch
    return None