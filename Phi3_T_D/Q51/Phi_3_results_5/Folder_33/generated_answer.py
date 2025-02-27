def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            key = normalize(s)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count > 85:
                return False
    return True