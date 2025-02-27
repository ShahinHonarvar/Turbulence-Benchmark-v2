from collections import defaultdict

def if_contains_anagrams(words):

    def sort_tuple(k, v):
        return (k[0], tuple(sorted(k[1].lower())))

    def check_anagrams(word_list):
        sorted_words = defaultdict(list)
        for word in word_list:
            if len(word) >= 3:
                sorted_word = tuple(sorted(word.lower()))
                sorted_words[sorted_word].append(word)
        anagram_count = sum((1 for entries in sorted_words.values() if len(entries) > 1))
        return anagram_count // 2
    return check_anagrams(words) <= 8