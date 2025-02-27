from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    filtered_words = [word for word in words if len(word) >= 3 and word.isalpha()]
    normalized_words = [normalize(word) for word in filtered_words]
    counter = Counter(normalized_words)
    anagram_pairs = 0
    for count in counter.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 116