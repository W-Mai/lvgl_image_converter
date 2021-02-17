from lvgl_Converter import Converter

if __name__ == '__main__':
    f = r"E:\USERDATAS\Pictures\pig.png"

    c = Converter(f, "pig", True, Converter.FLAG.CF_TRUE_COLOR_332)
    c.convert(Converter.FLAG.CF_TRUE_COLOR_332)

