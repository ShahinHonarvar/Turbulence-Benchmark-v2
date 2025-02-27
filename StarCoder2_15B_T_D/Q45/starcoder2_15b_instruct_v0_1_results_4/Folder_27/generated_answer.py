import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    for i in range(2, 8):
        for j in range(i + 1, 8):
            for permutation in permutations(letters[i:j + 1]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes