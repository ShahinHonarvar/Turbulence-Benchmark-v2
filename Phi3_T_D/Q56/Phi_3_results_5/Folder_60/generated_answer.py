from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 36:
        return []
    seen_chars = defaultdict(bool)
    substr_set = set()
    for i in range(len(s) - 35):
        if all((seen_chars[c] == False for c in s[i:i + 36])):
            substr_set.add(s[i:i + 36])
            for c in s[i:i + 36]:
                seen_chars[c] = True
    return list(substr_set)