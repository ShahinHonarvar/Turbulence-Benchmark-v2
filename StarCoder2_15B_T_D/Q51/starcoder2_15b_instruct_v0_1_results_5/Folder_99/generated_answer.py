def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string2 = strings[j]
            if is_anagram(string1, string2):
                anagram_pairs += 1
                if anagram_pairs > 93:
                    return False
    return anagram_pairs <= 93

def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = ''.join((c for c in string1 if c.isalpha()))
    string2 = ''.join((c for c in string2 if c.isalpha()))
    if len(string1) >= 3 and len(string2) >= 3:
        return sorted(string1) == sorted(string2)
    else:
        return False