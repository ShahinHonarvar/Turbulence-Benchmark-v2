from collections import Counter

def if_contains_anagrams(word_list):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize_word(word) for word in word_list]
    word_count = Counter(normalized_words)
    return sum((count * (count - 1) // 2 for count in word_count.values() if count >= 2)) >= 155