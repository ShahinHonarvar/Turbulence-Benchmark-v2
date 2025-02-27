from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagram_pairs = set()
    for word in words:
        if len(word) >= 3 and word.isalpha():
            sorted_word = tuple(sorted(word))
            for other in words:
                if word != other and len(other) >= 3 and other.isalpha():
                    sorted_other = tuple(sorted(other))
                    if sorted_word == sorted_other:
                        anagram_pairs.add((min(word, other), max(word, other)))
    return len(anagram_pairs) <= 36