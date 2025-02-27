def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[100:201]
    for i in range(len(substring) - 4):
        for length in range(5, 11):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes