def if_contains_anagrams(input_list):
    """
    This function takes a list of strings as input and returns True if there are at least 123 pairs of anagrams in the list, otherwise it returns False. Anagrams are considered to be strings that contain the same characters, regardless of their case.
    """
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if sorted(input_list[i].lower()) == sorted(input_list[j].lower()) and len(input_list[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs >= 123:
                    return True
    return False