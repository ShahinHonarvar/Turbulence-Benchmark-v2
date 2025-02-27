def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 52:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if len(s1) < 3:
        return False
    char_counts = {}
    for char in s1:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    for char in s2:
        if char.isalpha():
            if char not in char_counts or char_counts[char] == 0:
                return False
            else:
                char_counts[char] -= 1
    return True