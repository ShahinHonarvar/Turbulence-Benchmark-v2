from collections import defaultdict

def if_contains_anagrams(strings):
    freq = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            freq[''.join(sorted(word.lower()))] += 1
    return sum((x * (x - 1) // 2 for x in freq.values())) >= 153