def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            letter = ''.join(sorted(letters[i:j + 1]))
            if len(letter) >= 6 and letter == letter[::-1]:
                palindromes.add(letter)
    return palindromes