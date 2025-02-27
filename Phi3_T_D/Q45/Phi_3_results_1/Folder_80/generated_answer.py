from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    letters = [c.lower() for c in s[3:9]]
    unique_letters = ''.join(set(letters))
    palindromes = set()
    for i in range(7, 9):
        for perm in permutations(unique_letters, i):
            for combo in combinations(perm, i):
                word = ''.join(combo)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes