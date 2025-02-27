def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower())[:len(s)])
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1 and len(anagrams[key][0]) >= 3:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 143