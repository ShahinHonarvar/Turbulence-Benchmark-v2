def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) >= 3:
            key = normalize(s)
            if key in anagrams:
                count += anagrams[key]
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return count >= 91