from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s).lower())
    count = 0
    normalized_strings = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            normalized_strings[normalized].append(s)
    for anagrams in normalized_strings.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 177