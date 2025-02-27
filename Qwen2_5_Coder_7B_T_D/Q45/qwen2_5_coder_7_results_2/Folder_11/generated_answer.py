def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:8] if char.isalpha()]
    letter_freq = {}
    for letter in letters:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    result = set()
    for letter1 in letter_freq:
        for letter2 in letter_freq:
            if letter1 == letter2:
                if letter_freq[letter1] >= 4:
                    result.add(letter1 * 2)
            elif letter_freq[letter1] >= 2 and letter_freq[letter2] >= 2:
                result.add(letter1 * 2 + letter2 * 2)
    return result