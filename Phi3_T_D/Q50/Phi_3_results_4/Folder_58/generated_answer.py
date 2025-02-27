def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in anagrams:
            count += anagrams[norm]
            anagrams[norm] += 1
            if count + anagrams[norm] >= 411:
                return True
        else:
            anagrams[norm] = 1
    return False