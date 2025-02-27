from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagrams_count = defaultdict(int)
    for i, str1 in enumerate(strings):
        for str2 in strings[i + 1:]:
            if is_anagram(str1, str2):
                anagrams_count[tuple(sorted(str1.lower()))] += 1
    return sum((count >= 2 for count in anagrams_count.values())) >= 6