def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 116:
                    return False
    return True

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    if len(str1) < 3:
        return False
    for letter in str1:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    for letter in str2:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2