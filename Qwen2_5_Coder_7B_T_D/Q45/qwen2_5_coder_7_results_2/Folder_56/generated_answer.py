def palindromes_between_indices(s):
    letters = s[5:10].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n]
                            palindrome = palindrome + palindrome[:4][::-1]
                            palindromes.add(palindrome)
    return palindromes