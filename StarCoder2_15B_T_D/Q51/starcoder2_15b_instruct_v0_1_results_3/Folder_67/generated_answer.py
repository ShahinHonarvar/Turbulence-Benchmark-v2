from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    """
    Checks if the list of words contains at most 5 pairs of anagrams. An anagram is a
    word or phrase that is formed by rearranging the letters of another word or phrase.
    The function should only consider the anagrams of the English letters, and the anagrams
    of the length of at least three. The function should compare the strings in a
    case-insensitive manner.
    """
    anagrams = {}
    for word in words:
        word = word.lower()
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    num_anagrams = 0
    for key in anagrams:
        if len(anagrams[key]) >= 3:
            num_anagrams += len(anagrams[key]) - 2
    return num_anagrams <= 5