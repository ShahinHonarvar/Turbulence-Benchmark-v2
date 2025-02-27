import itertools

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    normalized_words = {normalize(word) for word in words if len(word) >= 3}
    anagrams_count = sum((1 for _ in itertools.combinations(normalized_words, 2) if _[0] == _[1]))
    return anagrams_count <= 15