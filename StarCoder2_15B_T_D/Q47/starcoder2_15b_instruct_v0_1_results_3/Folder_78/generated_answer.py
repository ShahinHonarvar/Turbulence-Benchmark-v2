def palindromes_of_specific_lengths(string):
    """
    Find all palindromes in a given string that are between 19 and 55 characters long,
    and occur within the substring from index 15 to index 72, both inclusive. Only
    consider palindromes consisting of English letters.
    """
    palindromes = set()
    substring = string[15:73]
    for i in range(len(substring) - 19):
        for length in range(19, 56):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes