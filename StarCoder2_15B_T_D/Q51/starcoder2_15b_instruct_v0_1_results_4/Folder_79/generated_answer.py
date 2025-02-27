def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 173:
                    return False
    return anagram_pairs <= 173

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    return False