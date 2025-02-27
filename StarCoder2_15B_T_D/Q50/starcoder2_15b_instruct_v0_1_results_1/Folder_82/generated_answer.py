def if_contains_anagrams(input_list):
    """
    Checks if the given list of strings contains at least 276 pairs of anagrams.
    Anagrams are considered to be strings that have the same letters, regardless of case.
    """
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) >= 3 and len(input_list[j]) >= 3:
                if sorted(input_list[i].lower()) == sorted(input_list[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs >= 276:
                        return True
    return False