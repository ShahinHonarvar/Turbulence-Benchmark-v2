from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):

    def sorted_english_letters(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    valid_anagrams = 0
    word_counts = Counter((sorted_english_letters(word) for word in words if len(word) >= 3))
    for pair in combinations(word_counts.values(), 2):
        valid_anagrams += pair[0] * pair[1]
        if valid_anagrams > 57:
            return False
    return True