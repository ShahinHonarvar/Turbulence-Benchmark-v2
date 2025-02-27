def palindromes_of_specific_lengths(string):
    sub_string = string[20:75]
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(sub_string) - length + 1):
            palindrome = sub_string[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes