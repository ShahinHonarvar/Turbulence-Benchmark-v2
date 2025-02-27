from itertools import combinations

def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return all((x == y for x, y in zip(s, s[::-1])))
    letters_only = ''.join(filter(str.isalpha, text.lower()))
    palindromes = set()
    for length in range(149, len(letters_only) + 1):
        for index_combination in combinations(range(len(letters_only)), length):
            substring = ''.join((letters_only[i] for i in index_combination))
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes