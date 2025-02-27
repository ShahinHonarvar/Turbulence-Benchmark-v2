def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[4:6].lower()
    if len(letters) < 2:
        return set()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(2):
                for l in range(2):
                    pal = unique_letters[i] * k + unique_letters[j] * l
                    if len(pal) >= 3 and pal == pal[::-1]:
                        palindromes.add(pal)
    return palindromes