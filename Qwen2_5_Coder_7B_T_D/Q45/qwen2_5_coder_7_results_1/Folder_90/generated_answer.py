def palindromes_between_indices(s):
    letters = s[:6].lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes