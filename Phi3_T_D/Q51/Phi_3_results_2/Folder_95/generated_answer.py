from collections import defaultdict

def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = defaultdict(int)
    for s in string_list:
        if len(s) >= 3:
            normalized = normalize(s)
            anagrams_count[normalized] += 1
    return sum((count * (count - 1) // 2 for count in anagrams_count.values())) <= 6