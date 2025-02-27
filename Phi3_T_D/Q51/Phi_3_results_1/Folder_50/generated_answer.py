def if_contains_anagrams(strings):

    def to_signature(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sig = to_signature(string)
        if sig in anagrams:
            anagrams[sig] += 1
            if anagrams[sig] == 2:
                return True
        else:
            anagrams[sig] = 1
    return final_anagram_count == 0 or final_anagram_count <= 47