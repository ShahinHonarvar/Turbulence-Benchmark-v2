import itertools

def palindromes_between_indices(s):
    palindromes = set()
    for combination in itertools.permutations(s[2:6], 5):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes