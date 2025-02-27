import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()

    def get_palindromes(start, end):
        palindromes = set()
        for center in range(start, end):
            left, right = (center, center)
            while left >= start and right <= end and (s[left] == s[right]):
                if 26 <= right - left + 1 <= 33:
                    palindromes.add(s[left:right + 1])
                left -= 1
                right += 1
            left, right = (center, center + 1)
            while left >= start and right <= end and (s[left] == s[right]):
                if 26 <= right - left + 1 <= 33:
                    palindromes.add(s[left:right + 1])
                left -= 1
                right += 1
        return palindromes
    s = re.sub('[^a-zA-Z]', '', s[65:99]).lower()
    return get_palindromes(0, len(s) - 1)