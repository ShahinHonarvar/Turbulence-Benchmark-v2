def all_substring_of_size_n(s: str) -> list:
    valid_substrings = []
    if len(s) < 70:
        return valid_substrings
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == 70:
            valid_substrings.append(substring)
    return valid_substrings