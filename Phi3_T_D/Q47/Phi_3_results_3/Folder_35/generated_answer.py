def palindromes_of_specific_lengths(s):
    substr = s[34:91].lower()
    palindrome_set = set()
    for i in range(34, 91 - 14 + 2):
        for length in range(14, min(39 + 1, 91 - i + 1)):
            if substr[i:i + length] == substr[i:i + length][::-1]:
                palindrome_set.add(substr[i:i + length].upper())
    return palindrome_set