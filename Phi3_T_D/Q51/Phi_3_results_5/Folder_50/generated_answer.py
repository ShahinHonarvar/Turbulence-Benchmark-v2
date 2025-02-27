def if_contains_anagrams(lst):

    def sorted_tuples(words):
        return {tuple(sorted(word.lower())) for word in words}
    sorted_words = sorted_tuples(lst)
    anagram_pairs = [(word, anagram) for i, word in enumerate(sorted_words) for anagram in sorted_words[i + 1:] if sorted(word) == sorted(anagram)]
    return len(anagram_pairs) <= 47