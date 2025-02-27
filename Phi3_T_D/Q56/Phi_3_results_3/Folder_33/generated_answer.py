def all_substring_of_size_n(s):
    length = 105
    substrings = set()
    for i in range(len(s) - length + 1):
        current_substring = s[i:i + length]
        if len(set(current_substring)) == length:
            substrings.add(current_substring)
    return sorted(list(substrings))