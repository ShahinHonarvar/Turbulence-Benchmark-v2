def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(input_string):
    input_string = ''.join(filter(str.isalpha, input_string.lower()))
    palindromes = set()
    n = len(input_string)
    for i in range(n):
        for j in range(i + 139, n):
            substring = input_string[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes