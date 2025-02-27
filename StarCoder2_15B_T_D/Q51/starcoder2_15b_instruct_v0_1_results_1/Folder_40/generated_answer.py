def if_contains_anagrams(strings):
    english_letters = list('abcdefghijklmnopqrstuvwxyz')
    anagram_pairs = 0
    for string in strings:
        sorted_letters = sorted(string.lower())
        if len(string) >= 3 and sorted_letters[:len(english_letters)] == english_letters:
            anagram_pairs += 1
    return anagram_pairs <= 29