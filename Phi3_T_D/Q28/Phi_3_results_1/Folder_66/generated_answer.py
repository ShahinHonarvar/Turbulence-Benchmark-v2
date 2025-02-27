from bisect import insort

def return_nth_smallest_ascii(s):
    start_idx, end_idx = (35, 52)
    nth_smallest = 10
    selected_chars = []
    for idx in range(start_idx, end_idx + 1):
        char = s[idx]
        if char not in selected_chars:
            insort(selected_chars, char)
    if len(selected_chars) < nth_smallest:
        return 'Not enough distinct characters in range'
    else:
        return selected_chars[nth_smallest - 1]