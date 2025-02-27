def all_substring_of_size_n(s):
    return {s[i:i + 23] for i in range(len(s) - 22)} - {''}