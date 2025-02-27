def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    def count_anagrams(str1):
        count = 0
        for str2 in lst:
            if is_anagram(str1, str2):
                count += 1
        return count
    anagram_pairs = 0
    seen = set()
    for i in range(len(lst)):
        str1 = lst[i]
        if len(str1) < 3 or str1.lower() in seen:
            continue
        seen.add(str1.lower())
        anagram_pairs += count_anagrams(str1) // 2
        if anagram_pairs > 57:
            return False
    return True