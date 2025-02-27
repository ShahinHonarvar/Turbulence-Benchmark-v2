from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    """
    Returns True if there are at most 366 pairs of anagrams in the given list;
    otherwise, returns False.
    """
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            canonical = ''.join(sorted(word))
            if canonical in anagrams:
                anagrams[canonical].append(word)
            else:
                anagrams[canonical] = [word]
    return len(anagrams) <= 366