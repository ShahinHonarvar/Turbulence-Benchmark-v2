from string import ascii_letters

def palindromes_of_specific_lengths(s):
    sub = s[:301]

    def is_palindrome(string):
        return string.lower() == string[::-1].lower()
    palindromes = set()
    for length in range(50, 61):
        for i in range(len(sub) - length + 1):
            substring = sub[i:i + length]
            if all((c in ascii_letters for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return {p.lower() for p in palindromes}