from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word] += 1
            count += anagrams[sorted_word] - 1
            if count >= 115:
                return True
    return False