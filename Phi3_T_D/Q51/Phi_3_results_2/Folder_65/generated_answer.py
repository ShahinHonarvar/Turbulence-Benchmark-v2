from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    sorted_words = {normalize(word) for word in words if len(word) >= 3}
    return sum((v for v in sorted_words.values() if v > 1)) <= 72