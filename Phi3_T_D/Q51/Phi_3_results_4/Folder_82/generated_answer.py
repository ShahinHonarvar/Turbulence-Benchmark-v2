def if_contains_anagrams(words):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count_pairs = 0
    seen = {}
    for word in words:
        if len(word) < 3:
            continue
        norm = normalize(word)
        if norm in seen:
            count_pairs += seen[norm]
            seen[norm] += 1
        else:
            seen[norm] = 1
        if count_pairs >= 40:
            return False
    return True