def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    unique_anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in unique_anagrams:
                unique_anagrams[sorted_str].append(s)
            else:
                unique_anagrams[sorted_str] = [s]
    anagram_pairs_count = 0
    for anagram_list in unique_anagrams.values():
        if len(anagram_list) > 1:
            anagram_pairs_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_pairs_count <= 58