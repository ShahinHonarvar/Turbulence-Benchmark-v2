def palindromes_between_indices(s):
    letters = s[4:9].lower()
    unique_letters = set(letters)
    length = len(unique_letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                for l in range(k + 1, length):
                    for m in range(l + 1, length):
                        palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[l] + unique_letters[k] + unique_letters[j] + unique_letters[i]
                        palindromes.add(palindrome)
    return palindromes