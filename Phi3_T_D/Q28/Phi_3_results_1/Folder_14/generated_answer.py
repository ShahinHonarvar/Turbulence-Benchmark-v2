def return_nth_smallest_ascii(s):
    i = 0
    distinct_chars = []
    for char in s[45:83]:
        if char not in distinct_chars:
            distinct_chars.append(char)
        i += 1
    distinct_chars.sort(key=lambda x: ord(x))
    return distinct_chars[15]