from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            count[sorted_word] += 1
    return sum((v * (v - 1) // 2 for v in count.values())) >= 188