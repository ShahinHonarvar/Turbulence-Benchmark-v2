def palindromes_between_indices(string):
    result = set()

    def find_palindromes(string, index):
        if index == len(string) // 2:
            result.add(string)
            return
        if string[index].lower() == string[-index - 1].lower():
            find_palindromes(string, index + 1)
    find_palindromes(string, 0)
    return result