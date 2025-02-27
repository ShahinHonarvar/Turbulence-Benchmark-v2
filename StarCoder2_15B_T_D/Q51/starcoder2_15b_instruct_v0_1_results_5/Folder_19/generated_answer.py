def if_contains_anagrams(input_list):
    """
    Returns true if there are at most 69 pairs of anagrams in the given list; otherwise, returns false.
    Only considers anagrams of the English letters. Only considers anagrams of length of at least three.
    """
    anagram_pairs = 0
    for i, word1 in enumerate(input_list):
        for j, word2 in enumerate(input_list):
            if i != j and is_anagram(word1, word2):
                anagram_pairs += 1
                if anagram_pairs > 69:
                    return False
    return True

def is_anagram(word1, word2):
    """
    Returns true if the two words are anagrams; otherwise, returns false.
    Only considers anagrams of the English letters. Only considers anagrams of length of at least three.
    """
    word1 = ''.join((c for c in word1.lower() if c.isalpha()))
    word2 = ''.join((c for c in word2.lower() if c.isalpha()))
    if len(word1) >= 3 and len(word2) >= 3:
        return sorted(word1) == sorted(word2)
    else:
        return False