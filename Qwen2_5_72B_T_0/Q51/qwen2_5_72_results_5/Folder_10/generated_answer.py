from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            for other in lst:
                if word != other and len(other) >= 3 and other.isalpha() and (normalize(other) == normalized_word):
                    anagram_pairs.add(tuple(sorted((word.lower(), other.lower()))))
    return len(anagram_pairs) <= 21