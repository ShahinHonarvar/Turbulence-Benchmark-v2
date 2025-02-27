from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized = {}
    for string in strings:
        if len(string) >= 3:
            norm_str = normalize(string)
            if norm_str in normalized:
                count += normalized[norm_str]
                normalized[norm_str] += 1
            else:
                normalized[norm_str] = 1
    count = count // 2
    return count <= 44