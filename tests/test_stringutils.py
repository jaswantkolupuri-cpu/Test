from toybox.stringutils import is_palindrome, reverse, slugify, word_count


def test_reverse():
    assert reverse("hello") == "olleh"


def test_is_palindrome_true():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_is_palindrome_false():
    assert not is_palindrome("hello")


def test_word_count():
    assert word_count("the quick brown fox") == 4


def test_slugify():
    assert slugify("Hello, World!") == "hello-world"
