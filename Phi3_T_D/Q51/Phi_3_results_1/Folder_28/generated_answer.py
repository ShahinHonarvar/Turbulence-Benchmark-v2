from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return Counter(s.lower())
    count = 0
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        for seen_word in seen:
            if norm_word == normalize(seen_word):
                count += 1
                break
        seen.add(word)
        if count > 78:
            return False
    return True