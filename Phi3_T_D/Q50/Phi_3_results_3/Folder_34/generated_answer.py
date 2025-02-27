from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower())).lstrip(' ')
        anagrams[sorted_str] += 1
    count = 0
    for key in anagrams:
        if len(key) >= 3 and anagrams[key] > 1:
            count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 25