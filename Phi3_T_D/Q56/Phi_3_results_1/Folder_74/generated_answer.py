def all_substring_of_size_n(s):
    size = 97
    if size > len(s):
        return []
    substrings = {s[i:i + size] for i in range(len(s) - size + 1) if len(set(s[i:i + size])) == size}
    return list(substrings)