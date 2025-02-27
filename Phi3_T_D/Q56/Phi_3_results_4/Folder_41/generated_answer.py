def all_substring_of_size_n(s):
    valid_substrings = set()
    N = len(s)
    target_len = 74
    if N < target_len:
        return list(valid_substrings)
    seen = set()
    for i in range(N - target_len + 1):
        substring = s[i:i + target_len]
        if len(set(substring)) == target_len and substring not in seen:
            valid_substrings.add(substring)
            seen.add(substring)
    return list(valid_substrings)