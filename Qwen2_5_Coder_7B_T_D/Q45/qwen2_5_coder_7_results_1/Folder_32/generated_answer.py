from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    result = set()
    for i in range(1, 8):
        for j in range(i + 4, 8):
            sub_str = s[i:j + 1]
            counter = Counter(sub_str.lower())
            for perm in permutations(counter.elements()):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
    return result