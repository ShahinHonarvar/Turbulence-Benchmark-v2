def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3)
    counts = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        counts[key] = counts.get(key, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values() if count >= 2))
    return anagram_pairs <= 28