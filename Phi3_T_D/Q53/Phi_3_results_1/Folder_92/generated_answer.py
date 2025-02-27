from itertools import combinations

def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1] and all(('a' <= c <= 'z' for c in s))

    def find_palindromes(sub):
        return {sub[i:j] for i, j in combinations(range(len(sub) + 1), r=2) if j - i >= 10 and is_palindrome(sub[i:j])}
    input_string = input_string.lower()
    palindromes = set()
    for word in input_string.split():
        palindromes.update(find_palindromes(word))
    return palindromes