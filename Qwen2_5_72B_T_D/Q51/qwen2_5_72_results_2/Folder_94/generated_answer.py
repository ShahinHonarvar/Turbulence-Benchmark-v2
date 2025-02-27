def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1) == sorted(str2)
    strings = [s.lower() for s in strings if s.isalpha()]
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs.add(tuple(sorted((strings[i], strings[j]))))
    return len(anagram_pairs) <= 181