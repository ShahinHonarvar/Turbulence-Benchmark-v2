from string import ascii_letters

def palindromes_of_specific_lengths(s):
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:10].lower()
    for i in range(3, 6):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((c in ascii_letters for c in substring)) and is_palindrome(substring):
                result.add(substring)
    return result