def if_contains_anagrams(strings):

    def to_signature(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sig = to_signature(string)
        if sig in anagrams:
            anagrams[sig].append(string)
        else:
            anagrams[sig] = [string]
    count = sum((len(lst) // 2 for lst in anagrams.values() if len(lst) > 1))
    return count >= 68