def if_contains_anagrams(words):

    def count_letters(word):
        letter_count = {}
        for letter in word.lower():
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1
        return letter_count
    anagrams_count = 0
    checked = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if (i, j) in checked or (j, i) in checked:
                continue
            word_a_count, word_b_count = (count_letters(words[i]), count_letters(words[j]))
            if word_a_count == word_b_count:
                anagrams_count += 1
                checked.add((i, j))
                checked.add((j, i))
            if anagrams_count > 84:
                return False
    return True