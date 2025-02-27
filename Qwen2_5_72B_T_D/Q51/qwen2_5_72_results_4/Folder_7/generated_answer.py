from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and s.isalpha():
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 445