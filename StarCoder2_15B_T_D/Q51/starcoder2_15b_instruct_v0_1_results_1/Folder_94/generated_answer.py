def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs <= 181

def are_anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if len(s1) < 3:
        return False
    char_counts = {}
    for char in s1:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    for char in s2:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1
    return all((count == 0 for count in char_counts.values()))