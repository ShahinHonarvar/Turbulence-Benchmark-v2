def palindromes_of_specific_lengths(string):
    sub_string = string[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(sub_string) - length + 1):
            palindrome = sub_string[i:i + length]
            if palindrome == palindrome[::-1]:
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes