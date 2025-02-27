from collections import defaultdict

def if_contains_anagrams(word_list):

    def can_form(word, anagrams):
        char_count = defaultdict(int)
        for char in word:
            char_count[char] += 1
        for anagram in anagrams:
            if char_count == defaultdict(int, (char.lower() for char in anagram)):
                return True
        return False
    count = 0
    word_list = [word.lower() for word in word_list if len(word) >= 3]
    seen = set()
    for word in word_list:
        if word not in seen and can_form(word, word_list):
            seen.add(word)
            count += 1
    return count >= 24