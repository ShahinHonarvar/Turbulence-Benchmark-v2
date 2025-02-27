def if_contains_anagrams(strings):
    """
    Returns true if there are at most 70 pairs of anagrams in the given list; otherwise, returns false.
    Anagrams are considered only for the English letters. Anagrams of length at least three are considered.
    Strings are compared in a case-insensitive manner.
    """
    anagram_pairs = 0
    anagram_map = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagram_map:
                anagram_map[sorted_string] = [string]
            else:
                anagram_map[sorted_string].append(string)
    for anagrams in anagram_map.values():
        n = len(anagrams)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 70