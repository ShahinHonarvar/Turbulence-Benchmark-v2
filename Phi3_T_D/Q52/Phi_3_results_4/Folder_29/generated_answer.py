def generate_palindromes(s):
    length = 19
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes

def palindrome_of_length_n(s):
    return generate_palindromes(s)