def palindrome_of_length_at_least_n(s):

    def find_palindromes(s, length):
        palindromes = set()
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
        return palindromes
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for n in range(137, len(s) + 1):
        palindromes.update(find_palindromes(s, n))
    return palindromes