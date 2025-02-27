from collections import defaultdict

def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    potential_pairs = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            normalized = normalize(s)
            potential_pairs[normalized].append(s)
    actual_pairs = 0
    for lst in potential_pairs.values():
        actual_pairs += sum((1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[i] != lst[j]))
    return actual_pairs >= 95