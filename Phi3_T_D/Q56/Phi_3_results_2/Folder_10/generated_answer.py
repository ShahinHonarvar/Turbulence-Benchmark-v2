def is_duplicate_free(substring):
    seen = set()
    for char in substring:
        if char in seen:
            return False
        seen.add(char)
    return True

def all_substring_of_size_n(s):
    if len(s) < 55:
        return []
    substrings = set()
    for i in range(len(s) - 54):
        substring = s[i:i + 55]
        if is_duplicate_free(substring):
            substrings.add(substring)
    return list(substrings)