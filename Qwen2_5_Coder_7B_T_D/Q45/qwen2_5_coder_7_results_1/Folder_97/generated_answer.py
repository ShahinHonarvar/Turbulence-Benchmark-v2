def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                candidate = letters[i] + letters[j] + letters[k]
                if candidate == candidate[::-1] and len(candidate) >= 3:
                    palindromes.add(candidate)
    return palindromes