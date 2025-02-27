def if_contains_anagrams(strings):
    letter_frequencies = dict.fromkeys(range(ord('a'), ord('z') + 1), 0)
    for string in strings:
        for letter in string.lower():
            if letter.isalpha():
                letter_frequencies[ord(letter)] += 1
    for frequency in letter_frequencies.values():
        if frequency > 26:
            return False
    return True