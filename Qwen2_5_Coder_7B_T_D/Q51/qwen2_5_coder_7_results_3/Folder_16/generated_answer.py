def if_contains_anagrams(lst):

    def count_anagrams(word):
        sorted_word = ''.join(sorted(word.lower()))
        return len([i for i in lst if sorted(i.lower()) == sorted_word and i.lower() != word])
    anagram_pairs = sum((count_anagrams(word) for word in lst if len(word) >= 3))
    return anagram_pairs <= 24