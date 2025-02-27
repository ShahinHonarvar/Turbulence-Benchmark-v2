def if_contains_anagrams(string_list):
    """
    Returns true if there are at most 97 pairs of anagrams in the given list;
    otherwise, returns false.
    """
    anagram_pairs = 0
    for i in range(len(string_list) - 1):
        for j in range(i + 1, len(string_list)):
            if are_anagrams(string_list[i], string_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 97:
                    return False
    return True

def are_anagrams(string1, string2):
    """
    Returns true if the given strings are anagrams; otherwise, returns false.
    """
    string1 = ''.join((c for c in string1 if c.isalpha())).lower()
    string2 = ''.join((c for c in string2 if c.isalpha())).lower()
    if len(string1) != len(string2):
        return False
    letter_counts = {}
    for letter in string1:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    for letter in string2:
        if letter not in letter_counts:
            return False
        else:
            letter_counts[letter] -= 1
            if letter_counts[letter] == 0:
                del letter_counts[letter]
    return len(letter_counts) == 0