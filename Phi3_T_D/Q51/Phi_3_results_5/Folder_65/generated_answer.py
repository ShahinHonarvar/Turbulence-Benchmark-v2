from collections import defaultdict

def if_contains_anagrams(strings):
    count_anagrams = 0
    letter_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            s_lower = s.lower()
            count = [letter_count[ord(char) - ord('a')] for char in s_lower]
            if count == sorted(count):
                count_anagrams += 1
                for i in range(len(s)):
                    letter_count[ord(s_lower[i]) - ord('a')] -= 1
    return count_anagrams <= 72