def if_contains_anagrams(words):
    """
    Returns True if there are at most 22 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are considered only for the English letters. Anagrams of length 3 or more are considered.
    Strings are compared in a case-insensitive manner.
    """
    anagram_groups = {}
    for word in words:
        canonical_word = ''.join(sorted(word.lower()))
        if len(canonical_word) >= 3:
            if canonical_word in anagram_groups:
                anagram_groups[canonical_word].append(word)
            else:
                anagram_groups[canonical_word] = [word]
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += len(group) - 1
    return anagram_count <= 22