def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i, string1 in enumerate(string_list):
        for j, string2 in enumerate(string_list):
            if i != j and are_anagrams(string1, string2):
                anagram_pairs += 1
                if anagram_pairs > 2:
                    return False
    return anagram_pairs <= 2

def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        return False
    letter_counts = {}
    for letter in string1:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    for letter in string2:
        if letter not in letter_counts:
            return False
        letter_counts[letter] -= 1
        if letter_counts[letter] == 0:
            del letter_counts[letter]
    return len(letter_counts) == 0