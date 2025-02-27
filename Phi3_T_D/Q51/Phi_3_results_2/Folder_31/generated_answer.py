def if_contains_anagrams(strings):

    def count_anagrams(s, anagrams):
        count = 0
        s_sorted = ''.join(sorted(s.lower()))
        for anagram in anagrams:
            if ''.join(sorted(anagram.lower())) == s_sorted and len(anagram) >= 3:
                count += 1
        return count
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            count += count_anagrams(strings[i], strings)
            if count > 65:
                return False
    return True