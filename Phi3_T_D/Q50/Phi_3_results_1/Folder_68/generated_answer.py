from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            count[sorted_s] += 1
    return sum((n * (n - 1) // 2 for n in count.values())) >= 9