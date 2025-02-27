def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    for i, first_word in enumerate(sorted_strings):
        for second_word in sorted_strings[i + 1:]:
            if first_word == second_word:
                anagram_pairs = sum((1 for s in sorted_strings if ''.join(sorted(s.lower())) == first_word))
                if anagram_pairs // 2 >= 74:
                    return True
    return False