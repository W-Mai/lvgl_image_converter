from typing import *

from PIL import Image


def getColorFromPalette(palette, index):
    return [palette[index + i] for i in range(3)]


class _const:
    class ConstError(TypeError):
        pass

    CF_TRUE_COLOR_332 = 0  # Helper formats. Used internally
    CF_TRUE_COLOR_565 = 1
    CF_TRUE_COLOR_565_SWAP = 2
    CF_TRUE_COLOR_888 = 3
    CF_ALPHA_1_BIT = 4
    CF_ALPHA_2_BIT = 5
    CF_ALPHA_4_BIT = 6
    CF_ALPHA_8_BIT = 7
    CF_INDEXED_1_BIT = 8
    CF_INDEXED_2_BIT = 9
    CF_INDEXED_4_BIT = 10
    CF_INDEXED_8_BIT = 11
    CF_RAW = 12
    CF_RAW_ALPHA = 13
    CF_RAW_CHROMA = 12

    CF_TRUE_COLOR = 100  # Helper formats is C arrays contains all true color formats (using in "download")
    CF_TRUE_COLOR_ALPHA = 101
    CF_TRUE_COLOR_CHROMA = 102

    def __setattr__(self, name, value):
        raise self.ConstError(f"Can't rebind const {name}")


class Converter(object):
    FLAG = _const()

    def __init__(self, path, out_name, dith: bool, cf):

        self.dith = None  # Dithering enable/disable
        self.w = None  # Image width
        self.h = None  # Image height
        self.cf = None  # Color format
        self.alpha = None  # Add alpha byte or not
        self.chroma = None  # Chroma keyed?
        self.d_out = None  # Output data (result)
        self.img = None  # Image resource
        self.out_name = None  # Name of the output file
        self.path = None  # Path to the image file

        # Helper variables
        self.r_act = None
        self.b_act = None
        self.g_act = None

        # For dithering
        self.r_earr = None  # Classification error for next row of pixels
        self.g_earr = None
        self.b_earr = None

        self.r_nerr = None  # Classification error for next pixel
        self.g_err = None
        self.b_nerr = None

        self.cf = cf
        self.dith = dith
        self.out_name = out_name
        self.path = path

        if cf == "raw" or cf == "raw_alpha" or cf == "raw_chroma":
            return
        self.img: Image.Image = Image.open(path)
        self.w, self.h = self.img.size

        if self.dith:
            self.r_earr = [0] * (self.w + 2)
            self.g_earr = [0] * (self.w + 2)
            self.b_earr = [0] * (self.w + 2)

        self.r_nerr = 0
        self.g_nerr = 0
        self.b_nerr = 0

    # noinspection PyAttributeOutsideInit
    def convert(self, cf, alpha: int = 0) -> NoReturn:
        self.cf = cf
        self.d_out = []
        self.alpha = alpha

        if self.cf == self.FLAG.CF_RAW or self.cf == self.FLAG.CF_RAW_ALPHA or self.cf == self.FLAG.CF_RAW_CHROMA:
            with open(self.path, "rb") as f:
                self.d_out = f.read()
            return

        palette_size = {
            self.FLAG.CF_INDEXED_1_BIT: 2,
            self.FLAG.CF_INDEXED_2_BIT: 4,
            self.FLAG.CF_INDEXED_4_BIT: 16,
            self.FLAG.CF_INDEXED_8_BIT: 256,
        }.get(self.cf, 0)

        if palette_size:
            img_tmp = Image.new("RGB", (self.w, self.h))
            img_tmp.paste(img_tmp, self.img)
            img_tmp = img_tmp.convert(mode="P", colors=palette_size)
            real_palette_size = self.img.getcolors()  # The real number of colors in the image's palette
            real_palette = self.img.getpalette()
            for i in range(palette_size):
                if i < real_palette_size:
                    c = getColorFromPalette(real_palette, i)
                    self.d_out.extend(c)
                    self.d_out.append(0xFF)
                else:
                    self.d_out.extend([0xFF, 0xFF, 0xFF, 0xFF])

            # Convert all the pixels
            for y in range(self.h):
                self._dith_reset()
                for x in range(self.w):
                    self._conv_px(x, y)

            # Revert the original image if it was converted to indexed
            if palette_size:
                self.img.paste(img_tmp)

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
