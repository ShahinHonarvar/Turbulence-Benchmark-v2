def palindromes_between_indices(s):
    s = s[4:10].lower()
    if len(s) < 4:
        return set()
    letters = sorted(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = ''.join(letters[i:j])
            if sub == sub[::-1] and len(sub) == len(set(sub)):
                palindromes.add(sub)
    return palindromes