def all_substring_of_size_n(text: str) -> list:
    n = 149
    all_substrings = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(set(substring)) == n:
            all_substrings.add(substring)
    return list(all_substrings)