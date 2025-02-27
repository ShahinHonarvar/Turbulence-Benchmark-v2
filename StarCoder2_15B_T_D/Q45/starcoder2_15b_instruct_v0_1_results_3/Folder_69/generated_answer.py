import itertools

def palindromes_between_indices(string):
    letters = sorted(set(string[0:4].lower()))
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes