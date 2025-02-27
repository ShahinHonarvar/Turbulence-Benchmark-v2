def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[29:97]
    for i in range(len(substring) - 11):
        for j in range(i + 12, min(i + 19, len(substring))):
            palindrome = substring[i:j]
            if palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes