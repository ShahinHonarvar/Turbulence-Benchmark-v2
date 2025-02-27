from collections import Counter

def if_contains_anagrams(strings):

    def normalized_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            norm = normalized_string(string)
            if norm in anagrams:
                anagrams[norm].append(string)
            else:
                anagrams[norm] = [string]
    count = sum((len(lst) // 2 for lst in anagrams.values() if len(lst) > 2))
    return count >= 89