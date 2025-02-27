def if_contains_anagrams(words):
    anagrams_count = 0
    letters_set = set()
    for word in words:
        sorted_word = ''.join(sorted(word.lower())).lstrip('aouei')
        if sorted_word in letters_set:
            anagrams_count += 1
        else:
            letters_set.add(sorted_word)
    return anagrams_count <= 43