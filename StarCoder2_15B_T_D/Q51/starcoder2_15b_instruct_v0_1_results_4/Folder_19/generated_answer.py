def if_contains_anagrams(input_list):
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                anagram_count += 1
                if anagram_count > 69:
                    return False
    return True

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) >= 3 and len(s2) >= 3:
        return sorted(s1) == sorted(s2)
    else:
        return False