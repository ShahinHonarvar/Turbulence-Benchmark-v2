def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
            if len(anagrams[sorted_word]) >= 3:
                return True
        else:
            anagrams[sorted_word] = [word]
    return False