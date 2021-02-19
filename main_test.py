from lvgl_Converter import Converter


def test_main():
    assert 1


def test_c_array1():
    x_end = 5
    y_end = 5
    tmpArr = list(map(str, range(x_end * y_end)))
    tmpStr = ''
    for y in range(y_end):
        tmpStr += ', '.join(tmpArr[y * x_end: (y + 1) * x_end])
        tmpStr = ', '.join([tmpStr, '\n'])
    assert tmpStr == '''0, 1, 2, 3, 4, \n5, 6, 7, 8, 9, \n10, 11, 12, 13, 14, \n15, 16, 17, 18, 19, \n20, 21, 22, 23, 24, \n'''


def test_c_array2():
    x_end = 16
    y_end = 1
    tmpArr = list(map(str, range(x_end * y_end)))
    tmpStr = ''
    print(', \n'.join([', '.join(tmpArr[(x_end // 8) * x: (x_end // 8) * x + 8]) for x in range(x_end // 8)]))
    # assert tmpStr == '''0, 1, 2, 3, 4, \n5, 6, 7, 8, 9, \n10, 11, 12, 13, 14, \n15, 16, 17, 18, 19, \n20, 21, 22, 23, 24, \n'''


if __name__ == '__main__':
    f = r"E:\USERDATAS\Pictures\pig.png"

    c = Converter(f, "pig", True, Converter.FLAG.CF_TRUE_COLOR_332)
    c.convert(Converter.FLAG.CF_TRUE_COLOR_332)
    print(c.get_c_header())
    # print(c.format_to_c_array())
    print(c.get_c_footer(Converter.FLAG.CF_TRUE_COLOR_332))

    # test_c_array1()
    test_c_array2()
