from collections import defaultdict

def if_contains_anagrams(strings):

    def compare_no_whitespace(s1, s2):
        return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())
    anagram_count = 0
    anagrams_dict = defaultdict(int)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if compare_no_whitespace(strings[i], strings[j]):
                anagrams_dict[''.join(sorted(strings[i].replace(' ', '').lower()))] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams_dict.values() if len(anagrams_dict) >= 3))
    return pairs >= 108