from typing import *
from PIL import Image

class _const:
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


class Converter(object):
    FLAG = _const()
    FLAG.CF_TRUE_COLOR_332 = 0  # Helper formats. Used internally
    FLAG.CF_TRUE_COLOR_565 = 1
    FLAG.CF_TRUE_COLOR_565_SWAP = 2
    FLAG.CF_TRUE_COLOR_888 = 3
    FLAG.CF_ALPHA_1_BIT = 4
    FLAG.CF_ALPHA_2_BIT = 5
    FLAG.CF_ALPHA_4_BIT = 6
    FLAG.CF_ALPHA_8_BIT = 7
    FLAG.CF_INDEXED_1_BIT = 8
    FLAG.CF_INDEXED_2_BIT = 9
    FLAG.CF_INDEXED_4_BIT = 10
    FLAG.CF_INDEXED_8_BIT = 11
    FLAG.CF_RAW = 12
    FLAG.CF_RAW_ALPHA = 13
    FLAG.CF_RAW_CHROMA = 12

    FLAG.CF_TRUE_COLOR = 100  # Helper formats is C arrays contains all treu color formats (usin in "download")
    FLAG.CF_TRUE_COLOR_ALPHA = 101
    FLAG.CF_TRUE_COLOR_CHROMA = 102

    def __init__(self, path, out_name, dith, cf):
        self.dith = dith
        self.out_name = out_name
        self.


        pass

    def convert(self, cf, alpha: int = 0) -> NoReturn:
        pass

    def format_to_c_array(self) -> AnyStr:
        pass

    def get_c_header(self) -> AnyStr:
        pass

    def get_c_footer(self, cf) -> AnyStr:
        pass

    def download_c(self):
        pass

    def download_bin(self):
        pass

    def _conv_px(self, x, y):
        pass

    def _dith_reset(self):
        pass

    def _dith_next(self):
        pass

    def _classify_pixel(self):
        pass
