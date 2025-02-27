from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[6:10].lower()))
    count = Counter(letters)
    possible_chars = ''.join((char * (count[char] // 2) for char in count))
    palindromes = set()
    for perm in permutations(possible_chars):
        mid = ''
        if len(letters) % 2 == 1:
            for char in count:
                if count[char] % 2 == 1:
                    mid = char
                    break
        half_palindrome = ''.join(perm)
        palindrome = half_palindrome + mid + half_palindrome[::-1]
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes