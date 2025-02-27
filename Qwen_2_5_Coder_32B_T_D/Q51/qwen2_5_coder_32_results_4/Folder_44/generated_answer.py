from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    for key in anagrams:
        l = len(anagrams[key])
        if l > 1:
            count += l * (l - 1) // 2
            if count > 75:
                return False
    return True