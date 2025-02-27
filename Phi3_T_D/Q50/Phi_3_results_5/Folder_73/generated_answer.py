def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        norm_string = normalize(string)
        if norm_string in anagrams:
            anagrams[norm_string].append(string)
        else:
            anagrams[norm_string] = [string]
    count = 0
    for key in anagrams:
        pairs = len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        count += pairs
    return count >= 91