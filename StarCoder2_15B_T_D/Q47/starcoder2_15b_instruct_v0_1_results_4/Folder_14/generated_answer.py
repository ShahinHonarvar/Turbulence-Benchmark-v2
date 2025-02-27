def palindromes_of_specific_lengths(text):
    subtext = text[10:75]
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(subtext) - length + 1):
            palindrome = subtext[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes