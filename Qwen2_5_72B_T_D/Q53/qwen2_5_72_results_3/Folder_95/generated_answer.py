def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = len(input_string)
    for i in range(n):
        for j in range(i + 34, n):
            candidate = input_string[i:j + 1]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes