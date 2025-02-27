def find_palindromes(s):

    def is_palindrome(word):
        return word == word[::-1]
    all_palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 111, len(s)):
            potential_palindrome = s[i:j + 1]
            if is_palindrome(potential_palindrome):
                all_palindromes.add(potential_palindrome.lower())
    return all_palindromes

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s)