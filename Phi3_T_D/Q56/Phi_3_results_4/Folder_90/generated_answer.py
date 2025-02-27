def all_substring_of_size_n(s: str) -> list:
    result = []
    max_len = min(len(s), 130)
    for i in range(max_len):
        substring = s[i:i + 130]
        if len(set(substring)) == 130:
            result.append(substring)
    return result