def palindromes_between_indices(s):
    result = set()
    letters = s[:5].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 2:
        return result
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if candidate == candidate[::-1]:
                            result.add(candidate)
    return result