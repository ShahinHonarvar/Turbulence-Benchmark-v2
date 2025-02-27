def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    freq = {}
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in freq:
            freq[norm] += 1
        else:
            freq[norm] = 1
    count = 0
    for k in freq:
        count += freq[k] * (freq[k] - 1) // 2
        if count > 21:
            return False
    return True