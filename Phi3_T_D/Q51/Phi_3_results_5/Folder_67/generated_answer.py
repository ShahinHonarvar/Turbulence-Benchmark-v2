def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3) and (s1.lower() != s2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if (i, j) in checked_pairs or (j, i) in checked_pairs:
                continue
            if is_anagram(words[i], words[j]):
                anagram_count += 1
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
                if anagram_count > 5:
                    return False
    return True