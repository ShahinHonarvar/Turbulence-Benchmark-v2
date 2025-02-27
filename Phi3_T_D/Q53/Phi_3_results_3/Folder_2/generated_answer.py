def palindrome_of_length_at_least_n(s):

    def find_palindromes(subs):
        return set((sub for sub in set(subs) if len(sub) >= 55 and sub.lower() == sub[::-1].lower()))
    return find_palindromes(''.join([c if c.isalpha() else ' ' for c in s]).split())