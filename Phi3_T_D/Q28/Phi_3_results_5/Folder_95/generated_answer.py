def return_nth_smallest_ascii(s):
    assert 1 <= len(s) <= 100 and len(set(s)) == len(s) and (len(s) >= 46), 'Invalid input'
    filtered_chars = sorted([s[i] for i in range(1, 47)])
    return filtered_chars[12]