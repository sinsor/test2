def func(text):
    assert text.endswith(".abc")
    return text[:-4].capitalize()


def test_answer():
    print("the result is = {}".format(func("demir.xxx")))


def main():
    test_answer()


if __name__ == "__main__":
    main()
