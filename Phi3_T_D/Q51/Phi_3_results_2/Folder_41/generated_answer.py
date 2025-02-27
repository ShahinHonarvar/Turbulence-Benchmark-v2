from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        str1, str2 = (str1.lower(), str2.lower())
        return sorted(str1) == sorted(str2) and len(str1) >= 3
    anagram_counts = defaultdict(int)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                key = ''.join(sorted(strings[i]))
                anagram_counts[key] += 1
    return sum(anagram_counts.values()) <= 52