from collections import defaultdict

def if_contains_anagrams(lst):

    def count_anagrams(s, length):
        count = defaultdict(int)
        for i in range(len(s) - length + 1):
            sub = ''.join(sorted(s[i:i + length]))
            count[sub] += 1
        return sum((v * (v - 1) // 2 for v in count.values()))
    total = 0
    for s in lst:
        total += count_anagrams(s.lower(), 3)
    return total >= 91