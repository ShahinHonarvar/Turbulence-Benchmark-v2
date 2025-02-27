def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 188:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if len(s1) < 3:
        return False
    for letter in s1:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    for letter in s2:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return sorted(s1) == sorted(s2)