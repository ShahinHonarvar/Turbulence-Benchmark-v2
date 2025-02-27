def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[26:85]
    for i in range(len(substring) - 30):
        for j in range(30, 47):
            if substring[i:i + j] == substring[i:i + j][::-1]:
                palindrome = substring[i:i + j]
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes