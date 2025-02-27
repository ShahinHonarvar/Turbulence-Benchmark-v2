def all_substring_of_size_n(s: str) -> list:
    if len(s) < 34:
        return []
    substrings = set()
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if len(set(substring)) == 34:
            substrings.add(substring)
    return list(substrings)