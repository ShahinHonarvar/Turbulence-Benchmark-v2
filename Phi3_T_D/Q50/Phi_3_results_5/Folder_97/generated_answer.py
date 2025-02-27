from collections import defaultdict

def if_contains_anagrams(str_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    freq_map = defaultdict(int)
    for elem in str_list:
        if len(elem) >= 3:
            freq_map[normalize(elem)] += 1
    return sum((val // 2 for val in freq_map.values())) >= 123