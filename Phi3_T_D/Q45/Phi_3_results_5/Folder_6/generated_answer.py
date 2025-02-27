from itertools import permutations

def palindromes_between_indices(s):
    s_ = s[:8].lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(4, len(s_) + 1):
        for p in permutations(s_, i):
            possible_palindrome = ''.join(p)
            if is_palindrome(possible_palindrome):
                palindromes.add(possible_palindrome)
    return palindromes