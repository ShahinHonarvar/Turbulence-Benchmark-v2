from collections import defaultdict

def if_contains_anagrams(string_list):

    def count_chars(s):
        count = defaultdict(int)
        for char in s.lower():
            if char.isalpha():
                count[char] += 1
        return tuple(sorted(count.items()))
    string_count = defaultdict(int)
    for string in string_list:
        if len(string) >= 3:
            string_count[count_chars(string)] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in string_count.values()))
    return anagram_pairs >= 144