def func(text):
    assert text.endswith(".abc")
    return text[:-4].upper()


def test_answer():
    var = func("sadsadasdasdasdasdsadsadasd.abc")
    print("the result is = {}".format(var))
    with open('armut.txt', 'w+') as out:
        out.write(var + '\n')


def main():
    test_answer()


if __name__ == "__main__":
    main()
