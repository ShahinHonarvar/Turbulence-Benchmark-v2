def if_contains_anagrams(words):

    def get_signature(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        sig = get_signature(word)
        if sig in anagrams:
            anagrams[sig].append(word)
        else:
            anagrams[sig] = [word]
    anagram_pairs = [v[i:i + 2] for v in anagrams.values() for i in range(len(v) - 1)]
    return len(anagram_pairs) >= 34