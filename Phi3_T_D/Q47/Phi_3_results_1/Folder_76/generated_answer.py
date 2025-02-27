def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindrome = set()
    for length in range(154, 183):
        for i in range(101, 293 - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                palindrome.add(substr)
    return palindrome