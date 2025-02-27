from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sum((Counter(s1.lower()) - Counter(s2.lower())).values()) == 0 and len(s1) >= 3
    anagram_dict = defaultdict(list)
    for string in strings:
        signature = ''.join(sorted(string.lower()))
        anagram_dict[signature].append(string)
    anagram_pairs = 0
    for _, lst in anagram_dict.items():
        if len(lst) > 1:
            anagram_pairs += sum((is_anagram(lst[i], lst[j]) for i in range(len(lst)) for j in range(i + 1, len(lst))))
    return anagram_pairs <= 93