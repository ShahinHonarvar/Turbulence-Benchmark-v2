def find_palindromes(s, min_length):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + min_length, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s, 10)