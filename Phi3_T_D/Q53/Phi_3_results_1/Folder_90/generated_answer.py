import re
    from itertools import combinations

def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]

    def find_palindromes(chars):
        palindromes = set()
        for i in range(len(chars), 0, -1):
            for seq in combinations(chars, i):
                candidate = ''.join(seq)
                if is_palindrome(candidate):
                    palindromes.add(candidate.upper())
        return palindromes
    text = re.sub('[^a-zA-Z]', '', text)
    all_palindromes = find_palindromes(tuple(text))
    return {palindrome for palindrome in all_palindromes if len(palindrome) >= 140}