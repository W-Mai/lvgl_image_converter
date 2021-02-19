from lvgl_Converter import Converter


def test_main():
    assert 1


if __name__ == '__main__':
    f = r"E:\USERDATAS\Pictures\pig.png"

    c = Converter(f, "pig", True, Converter.FLAG.CF_TRUE_COLOR_332)
    c.convert(Converter.FLAG.CF_TRUE_COLOR_332)
    print(c.get_c_header())
    print(c.get_c_footer(Converter.FLAG.CF_ALPHA_1_BIT))

