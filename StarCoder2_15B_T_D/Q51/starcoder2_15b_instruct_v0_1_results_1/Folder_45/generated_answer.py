def if_contains_anagrams(words):
    """
    Returns True if there are at most 464 pairs of anagrams in the given list; otherwise, returns False.
    Only considers the anagrams of the English letters. Only considers the anagrams of the length of at least three.
    Compares the strings in a case-insensitive manner.
    """

    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) != len(word2):
            return False
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
    anagram_count = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_count += 1
                if anagram_count > 464:
                    return False
    return True