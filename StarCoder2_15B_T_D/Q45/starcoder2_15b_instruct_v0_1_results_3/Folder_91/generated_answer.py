import itertools

def palindromes_between_indices(string):
    letters = sorted(set(string[2:7].lower()))
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes