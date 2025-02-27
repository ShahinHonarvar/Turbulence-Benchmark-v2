def palindromes_between_indices(string):
    s = string[4:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            palindrome = s[i:j + 1]
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes