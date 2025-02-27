def all_substring_of_size_n(s):
    length = 127
    seen = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            seen.add(substring)
    return list(seen)