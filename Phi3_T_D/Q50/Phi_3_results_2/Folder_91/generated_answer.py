from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_counts = defaultdict(int)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_counts[tuple(sorted(strings[i].lower()))] += 1
    return sum((count >= 2 for count in anagram_counts.values())) // 2 >= 6