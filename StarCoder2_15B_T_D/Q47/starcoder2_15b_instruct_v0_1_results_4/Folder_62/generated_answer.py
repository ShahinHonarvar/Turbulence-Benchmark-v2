def palindromes_of_specific_lengths(string):
    substring = string[26:88]
    substring_lowercase = substring.lower()
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(substring_lowercase) - length + 1):
            palindrome = substring_lowercase[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes