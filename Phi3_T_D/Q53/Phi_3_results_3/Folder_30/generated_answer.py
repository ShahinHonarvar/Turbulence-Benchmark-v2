def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def longest_palindrome_substring(s):
    n = len(s)
    table = [[0 for x in range(n)] for y in range(n)]
    longest_length = 1
    start = 0
    for i in range(n):
        table[i][i] = True
    max_length = 1
    i = 0
    while i < n - 1:
        if s[i] == s[i + 1].lower():
            table[i][i + 1] = True
            start = i
            max_length = 2
        i += 1
    length = 3
    while length <= n:
        i = 0
        while i < n - length + 1:
            j = i + length - 1
            if s[i].lower() == s[j].lower() and table[i + 1][j - 1]:
                table[i][j] = True
                start = i
                max_length = length
            i += 1
        length += 1
    return s[start:start + max_length]

def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    n = len(input_string)
    for length in range(16, n + 1):
        for start in range(n - length + 1):
            potential_palindrome = input_string[start:start + length]
            if is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome.lower())
    return palindromes