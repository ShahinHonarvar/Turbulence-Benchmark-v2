def all_substring_of_size_n(s: str) -> list:
    if len(s) < 38:
        return []
    substrings = set()
    for i in range(len(s) - 38 + 1):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            substrings.add(substring)
    return list(substrings)