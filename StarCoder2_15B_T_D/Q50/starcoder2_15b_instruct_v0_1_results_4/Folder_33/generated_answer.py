def if_contains_anagrams(strings):
    anagrams = set()
    for word in strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                return True
            anagrams.add(sorted_word)
    return False