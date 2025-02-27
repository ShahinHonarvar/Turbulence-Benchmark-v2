def if_contains_anagrams(strings):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_counts = {}
    for string in strings:
        letter_counts[string] = {letter: string.lower().count(letter) for letter in letters}
    sorted_letters = {}
    for string in strings:
        sorted_letters[string] = sorted(letter_counts[string].items(), key=lambda x: x[1], reverse=True)
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted_letters[strings[i]] == sorted_letters[strings[j]]:
                anagram_pairs += 1
                if anagram_pairs > 73:
                    return False
    return anagram_pairs <= 73