from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    """
    Checks if the given list of words contains at least 209 pairs of anagrams.
    Only considers anagrams of length 3 or more. Case-insensitive comparison.
    """
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    num_pairs = 0
    for anagram in anagrams.values():
        num_pairs += len(anagram) // 2
    return num_pairs >= 209