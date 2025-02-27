from collections import Counter

def if_contains_anagrams(lst):

    def clean_word(word):
        return ''.join(sorted(word.lower()))
    word_counts = Counter((clean_word(word) for word in lst if len(word) >= 3))
    return any((count >= 2 for count in word_counts.values()))