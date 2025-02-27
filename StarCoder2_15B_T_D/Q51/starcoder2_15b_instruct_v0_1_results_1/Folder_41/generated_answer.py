def if_contains_anagrams(input_list):

    def is_anagram(s1, s2):
        s1_letters = sorted(s1.lower())
        s2_letters = sorted(s2.lower())
        return s1_letters == s2_letters

    def has_english_letters(s):
        return set(s.lower()).issubset(set('abcdefghijklmnopqrstuvwxyz'))

    def has_length_of_at_least_three(s):
        return len(s) >= 3
    anagram_count = 0
    for i, s1 in enumerate(input_list):
        for s2 in input_list[i + 1:]:
            if is_anagram(s1, s2) and has_english_letters(s1) and has_english_letters(s2) and has_length_of_at_least_three(s1) and has_length_of_at_least_three(s2):
                anagram_count += 1
                if anagram_count > 52:
                    return False
    return anagram_count <= 52