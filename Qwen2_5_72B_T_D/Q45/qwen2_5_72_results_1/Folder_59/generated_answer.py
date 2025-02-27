from collections import Counter

def palindromes_between_indices(s):
    substring = s[8:10]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    palindromes = set()
    if not odd_chars:
        for char, count in counter.items():
            if count // 2 >= 1:
                palindrome = char * (count // 2) + (char * (count // 2))[::-1]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
                    palindromes.add(palindrome.upper())
                    palindromes.add(palindrome.capitalize())
    else:
        for char, count in counter.items():
            if count // 2 >= 1:
                palindrome = char * (count // 2) + odd_chars[0] + (char * (count // 2))[::-1]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
                    palindromes.add(palindrome.upper())
                    palindromes.add(palindrome.capitalize())
    return palindromes