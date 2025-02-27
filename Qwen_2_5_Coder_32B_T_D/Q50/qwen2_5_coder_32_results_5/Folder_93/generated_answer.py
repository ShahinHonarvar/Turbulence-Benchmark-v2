from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    seen = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            count += seen[w]
            seen[w] += 1
    return count >= 18