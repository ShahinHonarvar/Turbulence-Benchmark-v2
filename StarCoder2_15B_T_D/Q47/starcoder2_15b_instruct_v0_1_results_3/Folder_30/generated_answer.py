def palindromes_of_specific_lengths(string):
    sub_string = string[14:91]
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(sub_string) - length + 1):
            palindrome = sub_string[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes