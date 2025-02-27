from collections import defaultdict

def if_contains_anagrams(strings):
    string_dict = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and s.isalpha():
            s_sorted = ''.join(sorted(s))
            string_dict[s_sorted] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in string_dict.values()))
    return anagram_pairs <= 416