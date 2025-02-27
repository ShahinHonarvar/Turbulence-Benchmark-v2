def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[:8]
    for i in range(len(substring) - 3):
        for j in range(i + 3, i + 5):
            palindrome = substring[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes