from collections import defaultdict

def if_contains_anagrams(lst):

    def is_valid_anagram(s1, s2):
        return len(s1) >= 3 and s1.lower() == s2.lower()[::-1]
    anagrams_count = defaultdict(int)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_valid_anagram(lst[i], lst[j]):
                anagrams_count[lst[i].lower()] += 1
                anagrams_count[lst[j].lower()] += 1
    return sum((value // 2 for value in anagrams_count.values())) <= 9