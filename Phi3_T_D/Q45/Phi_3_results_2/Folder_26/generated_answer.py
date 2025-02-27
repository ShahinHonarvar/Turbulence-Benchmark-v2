from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    start_index = 4
    end_index = 6
    sub_str = s[start_index:end_index + 1]
    letters = set(sub_str.lower())
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for permutation in permutations(letters, length):
            if is_palindrome(''.join(permutation)):
                palindromes.add(''.join(permutation))
    return palindromes