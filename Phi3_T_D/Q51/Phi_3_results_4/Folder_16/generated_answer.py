from collections import Counter

def if_contains_anagrams(strings):

    def count_anagram_pairs(s1, s2):
        c1, c2 = (Counter(s1.lower()), Counter(s2.lower()))
        return len([ch for ch in s1 if c1[ch] == c2.get(ch, 0)])

    def is_anagram(s1, s2):
        return count_anagram_pairs(s1, s2) == len(s1) >= 3
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 24:
                    return False
    return True