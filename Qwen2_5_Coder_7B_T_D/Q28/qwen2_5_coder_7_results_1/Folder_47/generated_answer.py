def return_nth_smallest_ascii(s):
    selected_chars = [s[i] for i in range(3, 53) if i < len(s)]
    selected_chars.sort(key=lambda x: ord(x))
    return selected_chars[7]