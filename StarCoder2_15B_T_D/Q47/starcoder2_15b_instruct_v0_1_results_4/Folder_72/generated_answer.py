def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[26:91]
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes