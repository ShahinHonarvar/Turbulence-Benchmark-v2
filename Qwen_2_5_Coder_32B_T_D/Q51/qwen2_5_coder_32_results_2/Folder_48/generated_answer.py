from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    seen = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        seen[sorted_word] += 1
        if seen[sorted_word] > 1:
            count += seen[sorted_word] - 1
    return count <= 277