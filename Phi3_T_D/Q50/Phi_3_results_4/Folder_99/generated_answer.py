from collections import defaultdict

def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = defaultdict(int)
    for s in string_list:
        if len(s) >= 3:
            counts[normalize(s)] += 1
    return sum((count * (count - 1) // 2 for count in counts.values())) >= 314