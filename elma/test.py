def func(x):
    assert (x > 2)
    return x + 1


def test_answer():
    print("the result is = {}".format(func(3)))


def main():
    test_answer()


if __name__ == "__main__":
    main()
