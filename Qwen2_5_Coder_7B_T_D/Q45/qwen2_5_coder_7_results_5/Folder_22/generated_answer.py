def palindromes_between_indices(s):
    letters = s[5:7]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n]
                            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                                palindromes.add(palindrome)
    return palindromes