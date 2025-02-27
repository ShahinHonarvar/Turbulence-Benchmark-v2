from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        count = defaultdict(int)
        for char in s:
            count[char.lower()] += 1
        return tuple(sorted(count.items()))
    sorted_words = sorted([(count_letters(word), word) for word in strings], key=lambda x: x[0])
    anagram_pairs = 0
    i = 0
    while i < len(sorted_words) - 1:
        if sorted_words[i][0] == sorted_words[i + 1][0]:
            anagram_pairs += 1
            i += 2
        else:
            i += 1
        if anagram_pairs >= 95:
            return True
    return False