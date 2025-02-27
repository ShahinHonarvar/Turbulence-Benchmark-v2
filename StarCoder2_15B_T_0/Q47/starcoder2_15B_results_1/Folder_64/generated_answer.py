def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:8]
    for i in range(len(substring) - 3):
        for j in range(i + 4, min(i + 6, len(substring))):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes