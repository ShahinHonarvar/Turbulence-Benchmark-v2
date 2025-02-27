def palindromes_between_indices(s):
    letters = s[7:10].lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in unique_letters:
        for j in unique_letters:
            for k in unique_letters:
                for l in unique_letters:
                    candidate = i + j + k + l
                    if candidate == candidate[::-1] and len(candidate) == 4:
                        palindromes.add(candidate)
    return palindromes