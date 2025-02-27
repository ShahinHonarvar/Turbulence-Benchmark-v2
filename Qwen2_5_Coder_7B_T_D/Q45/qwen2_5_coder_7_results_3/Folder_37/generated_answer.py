def palindromes_between_indices(s):
    letters = s[1:5]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        candidate = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m]
                        if candidate == candidate[::-1] and len(candidate) >= 5:
                            palindromes.add(candidate)
    return palindromes