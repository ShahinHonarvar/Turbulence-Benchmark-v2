def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 68:
                    return False
    return anagram_pairs <= 68

def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) >= 3 and len(string2) >= 3:
        return sorted(string1) == sorted(string2)
    else:
        return False