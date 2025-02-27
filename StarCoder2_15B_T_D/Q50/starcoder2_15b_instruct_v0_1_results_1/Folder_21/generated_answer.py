def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        s1_count = {}
        s2_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1
        for ch in s2:
            s2_count[ch] = s2_count.get(ch, 0) + 1
        return s1_count == s2_count
    num_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                num_anagrams += 1
    return num_anagrams >= 136