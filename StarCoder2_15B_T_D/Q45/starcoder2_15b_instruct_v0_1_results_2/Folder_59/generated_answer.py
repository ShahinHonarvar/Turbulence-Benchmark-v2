from itertools import permutations

def palindromes_between_indices(string):
    letters = [c for c in string[8:10].lower() if c.isalpha()]
    permutations_of_letters = set(permutations(letters))
    palindromes = set()
    for permutation in permutations_of_letters:
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes