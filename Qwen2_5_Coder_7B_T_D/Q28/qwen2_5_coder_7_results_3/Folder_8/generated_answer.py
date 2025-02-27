def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(60, 89) if s[i] in s]
    filtered_chars.sort(key=lambda x: ord(x))
    if len(filtered_chars) >= 7:
        return filtered_chars[6]
    else:
        return None