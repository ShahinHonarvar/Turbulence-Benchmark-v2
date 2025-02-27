from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_key = normalize(word)
            anagram_count[anagram_key] += 1
    return sum((n * (n - 1) // 2 for n in anagram_count.values())) <= 94