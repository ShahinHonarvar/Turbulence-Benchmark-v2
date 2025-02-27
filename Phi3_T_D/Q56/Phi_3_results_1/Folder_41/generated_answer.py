def all_substring_of_size_n(s):
    length = 74
    seen = set()
    all_substrings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length and substring not in seen:
            all_substrings.append(substring)
            seen.add(substring)
    return all_substrings