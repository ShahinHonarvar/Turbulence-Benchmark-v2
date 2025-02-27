def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        s1 = sorted(s1)
        s2 = sorted(s2)
        return s1 == s2
    frequencies = {}
    for string in strings:
        for seen_string in frequencies:
            if is_anagram(string, seen_string):
                frequencies[string] += 1
                break
        else:
            frequencies[string] = 1
    for frequency in frequencies.values():
        if frequency > 97:
            return False
    return True