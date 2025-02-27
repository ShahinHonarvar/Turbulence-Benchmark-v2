from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    sub_str = s[1:5]
    sub_str_chars = sorted(set(sub_str.lower()), key=str.lower)
    palindromes = set()
    for i in range(len(sub_str_chars)):
        for p in permutations(sub_str_chars, i):
            if is_palindrome(''.join(p)):
                palindrome = ''.join(p).capitalize()
                for j in range(5, len(sub_str_chars) + 1):
                    for perm in permutations(sub_str_chars, j):
                        if is_palindrome(''.join(perm[:len(p)] + p + perm[len(p):])):
                            palindrome += ''.join(perm)
                            palindromes.add(palindrome.capitalize())
    return palindromes