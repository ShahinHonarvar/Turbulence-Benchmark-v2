from collections import defaultdict

def if_contains_anagrams(strings):

    def freq_hash(s):
        return ''.join(sorted(s.lower()))
    freq_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            freq_dict[freq_hash(string)] += 1
    count_pairs = sum((v * (v - 1) // 2 for v in freq_dict.values()))
    return count_pairs <= 74