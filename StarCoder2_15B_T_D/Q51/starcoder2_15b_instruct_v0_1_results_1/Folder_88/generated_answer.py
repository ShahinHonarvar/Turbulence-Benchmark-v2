def if_contains_anagrams(strings):
    num_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                num_anagrams += 1
    return num_anagrams <= 407

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if len(s1) < 3:
        return False
    if set(s1) != set(s2):
        return False
    return True