def palindrome_of_length_n(string):
    length = 279
    start = 0
    palindromes = set()
    while start + length <= len(string):
        substr = string[start:start + length].lower()
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
        start += 1
    return palindromes