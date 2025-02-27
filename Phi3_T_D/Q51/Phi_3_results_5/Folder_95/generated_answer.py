from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        str1, str2 = (str1.lower().strip(), str2.lower().strip())
        return len(str1) >= 3 and len(str2) >= 3 and (Counter(str1) == Counter(str2))
    anagram_counter = 0
    checked_pairs = set()
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in checked_pairs or (j, i) in checked_pairs:
                continue
            if is_anagram(lst[i], lst[j]):
                anagram_counter += 1
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
    return anagram_counter <= 6