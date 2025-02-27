def if_contains_anagrams(strings_list):

    def count_letters(word):
        counter = {}
        for letter in word.lower():
            if letter.isalpha():
                counter[letter] = counter.get(letter, 0) + 1
        return counter
    anagram_count = {}
    for string in strings_list:
        if len(string) >= 3:
            str_letters = count_letters(string)
            anagram_key = tuple(sorted(str_letters.items()))
            anagram_count[anagram_key] = anagram_count.get(anagram_key, 0) + 1
    return sum((count for count in anagram_count.values() if count > 1)) <= 70