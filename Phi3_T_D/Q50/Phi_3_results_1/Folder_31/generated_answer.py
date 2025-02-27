from collections import defaultdict

def if_contains_anagrams(lst):

    def count_characters(s):
        count = defaultdict(int)
        for char in s.lower():
            if char.isalpha():
                count[char] += 1
        return frozenset(count.items())
    anagrams = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_key = count_characters(word)
            anagrams[anagram_key] += 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) >= 68