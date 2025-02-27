def palindromes_between_indices(s):
    subset = s[1:7].lower()
    letters = list(subset)
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            letter = unique_letters[i] + unique_letters[j]
            if letter == letter[::-1]:
                palindromes.add(letter)
            for k in range(j + 1, len(unique_letters)):
                letter = unique_letters[i] + unique_letters[j] + unique_letters[k]
                if letter == letter[::-1]:
                    palindromes.add(letter)
                for l in range(k + 1, len(unique_letters)):
                    letter = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l]
                    if letter == letter[::-1]:
                        palindromes.add(letter)
                    for m in range(l + 1, len(unique_letters)):
                        letter = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m]
                        if letter == letter[::-1]:
                            palindromes.add(letter)
                        for n in range(m + 1, len(unique_letters)):
                            letter = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n]
                            if letter == letter[::-1]:
                                palindromes.add(letter)
    return palindromes