def if_contains_anagrams(string_list):
    """
    Checks if there are at least 189 pairs of anagrams of length at least three in the given list.
    """
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 189