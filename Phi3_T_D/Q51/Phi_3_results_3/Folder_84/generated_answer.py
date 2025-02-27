def if_contains_anagrams(lst):

    def count_letter_frequency(s):
        freq = {}
        for char in s:
            if char.isalpha():
                char = char.lower()
                freq[char] = freq.get(char, 0) + 1
        return freq

    def are_anagrams(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return count_letter_frequency(str1) == count_letter_frequency(str2)
    anagram_pairs = 0
    checked = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]) and pair_not_checked(i, j, checked):
                anagram_pairs += 1
                add_pair_to_checked_set(i, j, checked)
                if anagram_pairs > 16:
                    return False
            elif are_anagrams(lst[j], lst[i]) and pair_not_checked(j, i, checked):
                anagram_pairs += 1
                add_pair_to_checked_set(j, i, checked)
                if anagram_pairs > 16:
                    return False
    return True

def pair_not_checked(i, j, checked):
    return (i, j) not in checked and (j, i) not in checked

def add_pair_to_checked_set(i, j, checked):
    checked.add((i, j))