def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized_strings = {normalize(s): [] for s in strings if len(s) >= 3}
    for s in strings:
        if len(s) >= 3:
            norm_s = normalize(s)
            normalized_strings[norm_s].append(s)
    for anagrams in normalized_strings.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 136