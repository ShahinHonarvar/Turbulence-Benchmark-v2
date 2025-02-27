def if_contains_anagrams(strings):

    def count_letter_frequency(s):
        freq = {}
        for char in s.lower():
            if char.isalpha():
                freq[char] = freq.get(char, 0) + 1
        return frozenset(freq.items())
    anagram_count = 0
    checked = set()
    for i, str1 in enumerate(strings):
        for j, str2 in enumerate(strings[i + 1:], start=i + 1):
            if (str1, str2) in checked or (str2, str1) in checked:
                continue
            if len(str1) >= 3 and len(str2) >= 3:
                if count_letter_frequency(str1) == count_letter_frequency(str2):
                    anagram_count += 1
                    checked.add((str1, str2))
            if anagram_count >= 38:
                return True
    return False