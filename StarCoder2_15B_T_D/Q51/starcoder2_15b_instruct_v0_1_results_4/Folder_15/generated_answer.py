def if_contains_anagrams(strings):
    anagram_count = 0

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        str1 = ''.join((c for c in str1 if c.isalpha()))
        str2 = ''.join((c for c in str2 if c.isalpha()))
        return sorted(str1) == sorted(str2)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
    return anagram_count <= 20