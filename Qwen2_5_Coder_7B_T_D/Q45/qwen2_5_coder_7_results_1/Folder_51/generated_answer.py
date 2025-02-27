def palindromes_between_indices(s):
    letters = s[3:6]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for letter1 in unique_letters:
        for letter2 in unique_letters:
            for letter3 in unique_letters:
                for letter4 in unique_letters:
                    for letter5 in unique_letters:
                        candidate = ''.join([letter1, letter2, letter3, letter4, letter5])
                        if candidate == candidate[::-1] and len(candidate) >= 3:
                            palindromes.add(candidate)
    return palindromes