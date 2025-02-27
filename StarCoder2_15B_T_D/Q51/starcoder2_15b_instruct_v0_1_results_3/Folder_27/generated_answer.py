import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        s = s.lower()
        key = ''.join(sorted(s))
        if len(s) >= 3 and key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 113