def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 72):
        for j in range(i + 20, i + 33):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes