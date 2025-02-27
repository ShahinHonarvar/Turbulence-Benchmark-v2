from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagram_count[''.join(sorted(s))] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_of_anagrams <= 69