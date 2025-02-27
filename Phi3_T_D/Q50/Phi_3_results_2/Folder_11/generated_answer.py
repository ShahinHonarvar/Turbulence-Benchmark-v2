def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    pairs = 0
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        if norm_word in seen:
            pairs += 1
            if pairs >= 28:
                return True
        else:
            seen.add(norm_word)
    return False