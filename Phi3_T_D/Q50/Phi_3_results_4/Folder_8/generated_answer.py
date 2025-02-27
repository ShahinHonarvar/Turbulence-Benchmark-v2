from collections import defaultdict

def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize_word(word)
            anagram_count[normalized] += 1
    return sum((count // 2 for count in anagram_count.values())) >= 85