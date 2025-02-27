from collections import defaultdict

def if_contains_anagrams(words):
    word_count = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if word_count[sorted_word] >= 1:
                return True
            word_count[sorted_word] += 1
    return False