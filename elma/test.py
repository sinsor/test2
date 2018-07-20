def func(text):
    assert text.endswith(".abc")
    return text[:-4].capitalize()


def test_answer():
    var = func("sadsadasdasdasdasdsadsadasd.abc")
    print("the result is = {}".format(var))
    with open('armut.txt', 'a') as out:
        out.write(var + '\n')


def main():
    test_answer()


if __name__ == "__main__":
    main()
