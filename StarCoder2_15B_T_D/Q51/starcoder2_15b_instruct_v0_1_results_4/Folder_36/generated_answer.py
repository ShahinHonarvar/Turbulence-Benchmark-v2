def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def if_contains_anagrams(words: list) -> bool:
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 25:
                    return False
    return True