import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    arrangements = itertools.permutations(letters, len(letters))
    palindromes = set()
    for arrangement in arrangements:
        arrangement_str = ''.join(arrangement)
        if is_palindrome(arrangement_str) and len(arrangement_str) >= 4:
            palindromes.add(arrangement_str)
    return palindromes