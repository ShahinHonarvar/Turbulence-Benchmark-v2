def all_substring_of_size_n(s: str) -> list:
    n = 64
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.add(substring)
    return list(result)