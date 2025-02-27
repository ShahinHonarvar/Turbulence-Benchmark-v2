def if_contains_anagrams(strings):
    pairs_of_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                pairs_of_anagrams += 1
                if pairs_of_anagrams > 75:
                    return False
    return pairs_of_anagrams <= 75

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    count = [0] * 26
    for c in s1:
        if not c.isalpha():
            continue
        count[ord(c) - ord('a')] += 1
    for c in s2:
        if not c.isalpha():
            continue
        count[ord(c) - ord('a')] -= 1
    return all((c == 0 for c in count))