from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:7]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]

    def generate_palindromes(counter):
        if not counter:
            return set()
        palindromes = set()
        for char in counter:
            if counter[char] > 1:
                counter[char] -= 2
                for sub_palindrome in generate_palindromes(counter):
                    palindromes.add(char + sub_palindrome + char)
                counter[char] += 2
        if not palindromes:
            palindromes = {''} if not odd_chars else set(odd_chars)
        return palindromes
    valid_palindromes = {palindrome for palindrome in generate_palindromes(counter) if len(palindrome) >= 3}
    return valid_palindromes