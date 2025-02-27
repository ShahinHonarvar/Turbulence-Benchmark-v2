def if_contains_anagrams(list_of_strings):
    """
    Returns true if there are at most 65 pairs of anagrams in the given list; otherwise, returns false.
    Only considers anagrams of the English letters.
    Only considers anagrams of the length of at least three.
    Compares strings in a case-insensitive manner.
    """
    char_set = set('abcdefghijklmnopqrstuvwxyz')
    filtered_list = [s for s in list_of_strings if set(s.lower()) <= char_set and len(s) >= 3]
    sorted_list = [sorted(s.lower()) for s in filtered_list]
    anagram_pairs = set()
    for i, sorted_string in enumerate(sorted_list):
        for j in range(i + 1, len(sorted_list)):
            if sorted_string == sorted_list[j]:
                anagram_pairs.add((filtered_list[i], filtered_list[j]))
    return len(anagram_pairs) <= 65