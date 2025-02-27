def palindromes_between_indices(s):
    letters = set(s[1:7].lower())
    if len(letters) < 7:
        return set()
    half_length = 7 // 2
    palindromes = set()
    for i in range(len(letters) - half_length + 1):
        for j in range(i + half_length, len(letters) + 1):
            prefix = ''.join(sorted(letters[i:j]))
            palindrome = prefix + prefix[::-1]
            if len(palindrome) == 7:
                palindromes.add(palindrome)
    return palindromes