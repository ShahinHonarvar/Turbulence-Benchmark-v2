from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            anagrams[sorted_chars(word)].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return anagram_pairs >= 64