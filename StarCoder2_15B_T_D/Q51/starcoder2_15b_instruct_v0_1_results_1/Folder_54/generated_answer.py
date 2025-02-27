def if_contains_anagrams(strings):
    """
    Returns True if there are at most 39 pairs of anagrams in the given list; otherwise, returns False.
    Only considers the anagrams of the English letters.
    Only considers the anagrams of the length of at least three.
    Compares the strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3 and key.isalpha():
            anagrams[key] = anagrams.get(key, 0) + 1
    return sum((1 for count in anagrams.values() if count > 1)) <= 39