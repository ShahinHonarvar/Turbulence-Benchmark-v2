def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and is_anagram(string1, string2):
                anagram_pairs += 1
    return anagram_pairs <= 206

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    letter_counts = {}
    for letter in s1:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    for letter in s2:
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False
        else:
            letter_counts[letter] -= 1
    return all((count == 0 for count in letter_counts.values()))