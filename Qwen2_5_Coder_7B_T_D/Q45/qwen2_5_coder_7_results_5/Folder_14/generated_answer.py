def palindromes_between_indices(s):
    result = set()
    letters = s[4:6].lower()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(len(letters)):
                for l in range(k, len(letters)):
                    candidate = letters[i] + letters[j] + letters[k] + letters[l]
                    if candidate == candidate[::-1] and len(candidate) >= 3:
                        result.add(candidate)
    return result