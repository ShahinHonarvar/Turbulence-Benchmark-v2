from collections import defaultdict

def if_contains_anagrams(strings):
    isograms = defaultdict(int)
    for s in strings:
        s_key = ''.join(sorted(s.lower()))
        isograms[s_key] += 1
    count = sum((v * (v - 1) // 2 for v in isograms.values() if isograms[s_key] >= 3))
    return count >= 144