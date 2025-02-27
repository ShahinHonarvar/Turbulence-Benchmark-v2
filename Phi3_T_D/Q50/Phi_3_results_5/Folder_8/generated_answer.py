from collections import defaultdict

def if_contains_anagrams(str_list):

    def count_sorted_str(s):
        return (''.join(sorted(s.lower())), len(s) >= 3)
    sorted_str_dict = defaultdict(int)
    for s in str_list:
        key, is_valid = count_sorted_str(s)
        if is_valid:
            sorted_str_dict[key] += 1
    anagrams_count = sum((v * (v - 1) // 2 for v in sorted_str_dict.values()))
    return anagrams_count >= 85