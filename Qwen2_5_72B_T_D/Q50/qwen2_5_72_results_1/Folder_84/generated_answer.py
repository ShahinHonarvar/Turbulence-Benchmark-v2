from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counter = Counter()
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_counter[normalized_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return anagram_pairs >= 108