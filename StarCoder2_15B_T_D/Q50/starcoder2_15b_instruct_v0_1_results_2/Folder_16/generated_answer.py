def if_contains_anagrams(strings):
    """
    Checks if there are at least 155 pairs of anagrams in the given list of strings.
    The function only considers anagrams of length at least three.
    """
    anagram_pairs = 0
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    for group in anagrams.values():
        anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 155