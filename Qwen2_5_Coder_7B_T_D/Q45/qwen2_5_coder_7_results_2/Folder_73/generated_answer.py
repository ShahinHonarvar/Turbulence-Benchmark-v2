def palindromes_between_indices(s):
    letters = s[3:7]
    letters = letters.lower()
    unique_letters = set(letters)
    result = set()
    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters)):
            for k in range(j + 1, len(unique_letters)):
                for l in range(k + 1, len(unique_letters)):
                    for m in range(l + 1, len(unique_letters)):
                        for n in range(m + 1, len(unique_letters)):
                            for o in range(n + 1, len(unique_letters)):
                                for p in range(o + 1, len(unique_letters)):
                                    for q in range(p + 1, len(unique_letters)):
                                        palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n] + unique_letters[o] + unique_letters[p] + unique_letters[q]
                                        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                                            result.add(palindrome)
    return result