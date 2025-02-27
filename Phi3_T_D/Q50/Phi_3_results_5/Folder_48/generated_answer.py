from collections import defaultdict

def if_contains_anagrams(strings):

    def string_signature(s):
        return ''.join(sorted(s.lower()))
    string_hash = defaultdict(int)
    counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            signature = string_signature(s)
            string_hash[signature] += 1
            counts[string_hash[signature]] += 1
    return sum((v * (v - 1) // 2 for v in counts.values())) >= 219