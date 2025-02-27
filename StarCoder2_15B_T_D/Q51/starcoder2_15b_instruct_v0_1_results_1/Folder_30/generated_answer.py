def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 28:
                    return False
    return anagram_pairs <= 28

def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        return False
    letters = [0] * 26
    for char in string1:
        if not is_letter(char):
            continue
        index = ord(char) - ord('a')
        letters[index] += 1
    for char in string2:
        if not is_letter(char):
            continue
        index = ord(char) - ord('a')
        if letters[index] == 0:
            return False
        letters[index] -= 1
    return True

def is_letter(char):
    return ord('a') <= ord(char) <= ord('z')