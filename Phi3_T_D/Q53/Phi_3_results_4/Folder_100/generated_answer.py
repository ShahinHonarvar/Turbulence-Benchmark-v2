from itertools import combinations

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_lower = s.lower()
    candidate_words = set()
    for i in range(len(s_lower)):
        try:
            for j in range(i + 48, len(s_lower) + 1):
                word = s_lower[i:j]
                if all((c in alphabet for c in word)):
                    candidate_words.add(word)
        except IndexError:
            break
    return {word for word in candidate_words if is_palindrome(word)}