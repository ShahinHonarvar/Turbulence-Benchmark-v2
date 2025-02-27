def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s)).lower()
        if len(s) >= 3:
            if sorted_s in anagrams:
                count += anagrams[sorted_s]
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    return count >= 97