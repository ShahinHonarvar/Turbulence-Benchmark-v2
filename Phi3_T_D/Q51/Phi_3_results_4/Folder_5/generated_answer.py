def if_contains_anagrams(words):

    def clean_and_sort(word):
        return ''.join(sorted(word.lower()))
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = clean_and_sort(word)
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    count = sum((1 for count in anagrams.values() if count > 1))
    return count <= 4 * 2