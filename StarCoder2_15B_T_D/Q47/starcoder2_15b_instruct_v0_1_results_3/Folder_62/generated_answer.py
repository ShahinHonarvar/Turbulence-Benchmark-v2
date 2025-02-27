def palindromes_of_specific_lengths(string):
    if len(string) < 52:
        return set()
    substring = string[26:88]
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes