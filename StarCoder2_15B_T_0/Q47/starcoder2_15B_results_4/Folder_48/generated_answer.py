def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[155:284]
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes