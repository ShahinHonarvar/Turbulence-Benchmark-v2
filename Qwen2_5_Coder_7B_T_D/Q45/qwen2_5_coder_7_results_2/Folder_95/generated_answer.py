def palindromes_between_indices(s):
    letters = s[7:9]
    letters_lower = letters.lower()
    unique_letters = ''.join(sorted(set(letters_lower)))
    n = len(unique_letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(i, n):
                for l in range(i, n):
                    for m in range(i, n):
                        for o in range(i, n):
                            for p in range(i, n):
                                for q in range(i, n):
                                    for r in range(i, n):
                                        for s in range(i, n):
                                            palindrome = unique_letters[i] * 2 + unique_letters[j] * 2 + unique_letters[k] * 2 + unique_letters[l] * 2 + unique_letters[m] * 2 + unique_letters[n] * 2 + unique_letters[o] * 2 + unique_letters[p] * 2 + unique_letters[q] * 2 + unique_letters[r] * 2 + unique_letters[s] * 2
                                            if len(palindrome) >= 3 and palindrome.lower() == palindrome[::-1].lower():
                                                palindromes.add(palindrome)
    return palindromes