from Q45.starcoder2_15b_instruct_v0_1_results_3.Folder_1.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(7 + 1))
    if 7 - 4 + 1 < 5:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(5, 7 - 4 + 2)}


def test_string_of_distinct_chars():
    s = 'abcdefghijkl'
    assert not palindromes_between_indices(s)


def test_string_of_spaces():
    s = ' ' * (7 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_punctuations():
    s = '@' * (7 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_numbers():
    s = '0' * (7 * 2)
    assert not palindromes_between_indices(s)
        

def test_length_of_palindrome():
    s = ''.join('a' for _ in range(7 + 1))
    returned_result = palindromes_between_indices(s)
    for i in returned_result:
        assert 5 <= len(i) <= 7 - 4 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (7 + 1)
    ss = s[4:7 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 5:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 5)
        max_ = max(length, 5)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (7 + 1)
    ss = s[4:7 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 5:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 5)
        max_ = max(length, 5)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        