from collections import Counter

def if_contains_anagrams(str_list):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and s1.lower() != s2.lower() and (Counter(s1.lower()) == Counter(s2.lower()))
    anagrams_count = 0
    checked_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if (i, j) not in checked_pairs and is_anagram(str_list[i], str_list[j]):
                anagrams_count += 1
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
    return anagrams_count <= 10