from collections import defaultdict

def if_contains_anagrams(words):

    def get_sorted_signature(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagrams[get_sorted_signature(word)].append(word)
    anagram_pairs = sum((len(items) for items in anagrams.values())) // 2
    return anagram_pairs >= 50