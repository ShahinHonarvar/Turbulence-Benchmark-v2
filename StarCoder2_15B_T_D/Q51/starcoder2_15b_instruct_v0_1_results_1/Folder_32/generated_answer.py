import re

def if_contains_anagrams(strings):
    anagram_pairs = 0
    strings = [s.lower() for s in strings]
    strings.sort(key=lambda x: len(x))
    for i in range(len(strings) - 1):
        if len(strings[i]) < 3:
            continue
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            if sorted(re.sub('[^a-z]', '', strings[i])) == sorted(re.sub('[^a-z]', '', strings[j])):
                anagram_pairs += 1
                if anagram_pairs > 89:
                    return False
    return anagram_pairs <= 89