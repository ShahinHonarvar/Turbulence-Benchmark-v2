from collections import defaultdict

def if_contains_anagrams(lst):

    def generate_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for word in lst:
        length = len(word)
        if length < 3:
            continue
        key = generate_key(word)
        anagram_groups[key].append(word)
    count_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_groups.values()))
    return count_pairs <= 474