def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 3:
                    return False
    return anagram_pairs <= 3

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    char_count1 = {}
    for char in str1:
        if char.isalpha():
            if char not in char_count1:
                char_count1[char] = 0
            char_count1[char] += 1
    char_count2 = {}
    for char in str2:
        if char.isalpha():
            if char not in char_count2:
                char_count2[char] = 0
            char_count2[char] += 1
    return char_count1 == char_count2