from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize(word) for word in words]
    word_counts = Counter(normalized_words)
    count_of_anagrams = sum((1 for count in word_counts.values() if count > 1))
    return count_of_anagrams <= 416