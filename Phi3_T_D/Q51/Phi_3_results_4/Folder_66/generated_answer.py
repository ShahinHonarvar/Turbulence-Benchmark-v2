def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in strings:
        nw = normalize(word)
        if nw not in anagrams:
            anagrams[nw] = []
        anagrams[nw].append(word)
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        if n * (n - 1) // 2 > 64 * (n > 2):
            return False
        count += n * (n - 1) // 2
    return True