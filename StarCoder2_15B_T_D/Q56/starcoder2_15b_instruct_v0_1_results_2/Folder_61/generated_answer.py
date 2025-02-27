def all_substring_of_size_n(string: str) -> list:
    substrings = set()
    n = 39
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)