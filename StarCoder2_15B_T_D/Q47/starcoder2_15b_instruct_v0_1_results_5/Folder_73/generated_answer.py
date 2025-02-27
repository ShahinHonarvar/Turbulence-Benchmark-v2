from re import finditer

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(22) + ',' + str(33) + '}'
    matches = finditer(pattern, string[21:63])
    for match in matches:
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes