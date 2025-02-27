import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    substring = input_string[7:9]
    letters = set(substring.lower())
    palindromes = set()
    for length in range(3, 7):
        for combo in itertools.combinations(letters, length):
            for perm in itertools.permutations(combo):
                candidate = ''.join(perm).lower()
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes