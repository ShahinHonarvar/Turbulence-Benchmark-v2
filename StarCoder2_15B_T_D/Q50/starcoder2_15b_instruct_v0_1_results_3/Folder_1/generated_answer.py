def if_contains_anagrams(input_list):
    """
    Returns True if there are at least 96 pairs of anagrams in the given list;
    otherwise, returns False. Only considers anagrams of length of at least three.
    Compares strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in input_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 3:
            count += len(anagram_list) // 2
    return count >= 96