def all_substring_of_size_n(s):
    n = 47
    length = len(s)
    seen = set()
    distinct_substrings = set()
    for i in range(length - n + 1):
        current_substring = s[i:i + n]
        if len(set(current_substring)) == n:
            if current_substring not in seen:
                seen.add(current_substring)
                distinct_substrings.add(current_substring)
    return list(distinct_substrings)