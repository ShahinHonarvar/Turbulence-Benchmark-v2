import collections

def if_contains_anagrams(strings):
    count = 0
    strings = {str(sorted(s.lower())): 0 for s in strings if len(s) >= 3}
    for key in strings.keys():
        strings[key] += 1
        if strings[key] > 1:
            count += 1
    return count >= 64