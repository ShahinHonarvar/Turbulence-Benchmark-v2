def if_contains_anagrams(words):

    def sorted_and_stripped(word):
        return ''.join(sorted(word.lower())).lstrip('aouei')
    words_set = {sorted_and_stripped(word) for word in words if len(word) >= 3}
    unique_set = set(words_set)
    return len(unique_set) - len(words_set) <= 34