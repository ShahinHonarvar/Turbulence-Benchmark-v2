def if_contains_anagrams(lst):

    def count_letter_frequency(s):
        freq = {}
        for char in s.lower():
            if char.isalpha():
                freq[char] = freq.get(char, 0) + 1
        return freq

    def are_anagrams(str1, str2):
        freq1, freq2 = (count_letter_frequency(str1), count_letter_frequency(str2))
        return freq1 == freq2 and len(str1) >= 3 and (len(str2) >= 3)
    anagram_pairs = [(str1, str2) for i, str1 in enumerate(lst) for str2 in lst[i + 1:] if are_anagrams(str1, str2)]
    return len(anagram_pairs) >= 89