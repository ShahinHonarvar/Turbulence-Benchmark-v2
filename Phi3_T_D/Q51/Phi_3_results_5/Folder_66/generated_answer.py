from itertools import permutations
import string

def if_contains_anagrams(word_list):

    def normalize(word):
        return ''.join(sorted(word.lower())).replace(' ', '')

    def is_valid_word(word):
        return len(word) >= 3
    max_pairs = 64
    valid_words = [word for word in word_list if is_valid_word(word)]
    normalized_words = [normalize(word) for word in valid_words]
    anagram_count = 0
    for i in range(len(normalized_words)):
        for p in permutations(normalized_words[i], len(normalized_words[i])):
            if ''.join(p) in normalized_words and normalized_words.index(''.join(p)) != i:
                anagram_count += 1
                break
        if anagram_count > max_pairs:
            return False
    return True