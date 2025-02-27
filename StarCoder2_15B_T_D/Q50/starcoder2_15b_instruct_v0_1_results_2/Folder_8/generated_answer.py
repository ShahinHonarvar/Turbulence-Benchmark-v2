def if_contains_anagrams(strs):
    lowercase_strs = [s.lower() for s in strs]
    anagrams = {}
    for s in lowercase_strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 3:
            count += 1
    return count >= 85