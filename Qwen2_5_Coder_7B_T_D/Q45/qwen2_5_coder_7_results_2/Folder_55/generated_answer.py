def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = sorted(s)
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    for m in range(l, n):
                        for n in range(m, n):
                            word = ''.join(letters[i:j] + letters[j:k] + letters[k:l] + letters[l:m] + letters[m:n])
                            if word == word[::-1] and len(word) >= 3:
                                palindromes.add(word)
    return palindromes