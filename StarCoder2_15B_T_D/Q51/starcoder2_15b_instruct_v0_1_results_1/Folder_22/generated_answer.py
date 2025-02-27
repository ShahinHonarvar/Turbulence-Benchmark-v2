import re

def if_contains_anagrams(strings):
    words = [re.sub('[^a-zA-Z]', '', string).lower() for string in strings]
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    num_anagrams = sum((len(value) - 1 for value in anagrams.values()))
    return num_anagrams <= 14