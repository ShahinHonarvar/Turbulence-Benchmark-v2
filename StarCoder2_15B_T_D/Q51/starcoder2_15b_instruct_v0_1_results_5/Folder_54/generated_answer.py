def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

def is_valid_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return is_anagram(s1, s2) and len(s1) >= 3 and (len(s2) >= 3)

def count_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_valid_anagram(strings[i], strings[j]):
                count += 1
    return count

def if_contains_anagrams(strings):
    return count_anagrams(strings) <= 39