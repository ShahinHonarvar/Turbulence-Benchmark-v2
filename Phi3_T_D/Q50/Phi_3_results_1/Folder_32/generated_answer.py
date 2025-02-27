from collections import defaultdict

def if_contains_anagrams(words):

    def build_key(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_dict[build_key(word)] += 1
    anagram_pairs = sum((count // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 194