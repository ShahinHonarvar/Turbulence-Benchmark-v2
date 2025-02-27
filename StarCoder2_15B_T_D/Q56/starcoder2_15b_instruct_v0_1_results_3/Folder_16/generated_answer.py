def all_substring_of_size_n(s: str) -> [str]:
    if len(s) < 124:
        return []
    substrings = set()
    for i in range(len(s) - 124 + 1):
        substring = s[i:i + 124]
        if len(set(substring)) == 124:
            substrings.add(substring)
    return list(substrings)