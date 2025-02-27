from collections import defaultdict

def if_contains_anagrams(strings):

    def string_signature(s):
        return ''.join(sorted(s.lower()))
    freq = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            freq[string_signature(s)] += 1
    count = 0
    for n in freq.values():
        if n > 1:
            count += n * (n - 1) // 2
    return count <= 55