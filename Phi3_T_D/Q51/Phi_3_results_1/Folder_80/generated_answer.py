from collections import defaultdict

def if_contains_anagrams(strings):

    def isAnagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        if len(s1) != len(s2) or not all((c.isalpha() for c in s1)) or (not all((c.isalpha() for c in s2))):
            return False
        counter = defaultdict(int)
        for char in s1:
            counter[char] += 1
        for char in s2:
            counter[char] -= 1
        return all((val == 0 for val in counter.values()))
    anagram_pairs = [(strings[i], strings[j]) for i in range(len(strings)) for j in range(i + 1, len(strings)) if isAnagram(strings[i], strings[j]) and len(strings[i]) >= 3 and (len(strings[j]) >= 3)]
    return len(anagram_pairs) <= 255