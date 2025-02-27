from collections import defaultdict

def if_contains_anagrams(strings):

    def count_sorted(word):
        return ''.join(sorted(word.lower()))
    anagrams_count = 0
    word_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_word = count_sorted(string)
            anagrams_count += word_dict[sorted_word]
            word_dict[sorted_word] += 1
    return anagrams_count <= 277