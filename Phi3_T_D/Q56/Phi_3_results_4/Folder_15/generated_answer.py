from collections import defaultdict

def all_substring_of_size_n(s):
    length = 3
    if length > len(s):
        return []
    seen = defaultdict(bool)
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            if not seen[substring]:
                seen[substring] = True
                result.append(substring)
    return result