import os.path, sys, time
from lvgl_Converter import Converter
import msvcrt

color_format_dir = {
    "CF_TRUE_COLOR_332"             :Converter.FLAG.CF_TRUE_COLOR_332,  # Helper formats. Used internally
    "CF_TRUE_COLOR_565"             :Converter.FLAG.CF_TRUE_COLOR_565,
    "CF_TRUE_COLOR_565_SWAP"        :Converter.FLAG.CF_TRUE_COLOR_565_SWAP,
    "CF_TRUE_COLOR_888"             :Converter.FLAG.CF_TRUE_COLOR_888,
    "CF_ALPHA_1_BIT"                :Converter.FLAG.CF_ALPHA_1_BIT,
    "CF_ALPHA_2_BIT"                :Converter.FLAG.CF_ALPHA_2_BIT,
    "CF_ALPHA_4_BIT"                :Converter.FLAG.CF_ALPHA_4_BIT,
    "CF_ALPHA_8_BIT"                :Converter.FLAG.CF_ALPHA_8_BIT,
    "CF_INDEXED_1_BIT"              :Converter.FLAG.CF_INDEXED_1_BIT,
    "CF_INDEXED_2_BIT"              :Converter.FLAG.CF_INDEXED_2_BIT,
    "CF_INDEXED_4_BIT"              :Converter.FLAG.CF_INDEXED_4_BIT,
    "CF_INDEXED_8_BIT"              :Converter.FLAG.CF_INDEXED_8_BIT,
    "CF_RAW"                        :Converter.FLAG.CF_RAW,
    "CF_RAW_ALPHA"                  :Converter.FLAG.CF_RAW_ALPHA,
    "CF_RAW_CHROMA"                 :Converter.FLAG.CF_RAW_CHROMA,
    "CF_TRUE_COLOR"                 :Converter.FLAG.CF_TRUE_COLOR,  # Helper formats is C arrays contains all true color formats (using in "download")
    "CF_TRUE_COLOR_ALPHA"           :Converter.FLAG.CF_TRUE_COLOR_ALPHA,
    "CF_TRUE_COLOR_CHROMA"          :Converter.FLAG.CF_TRUE_COLOR_CHROMA,
}

cfg_en = {
    "yes"   : 1,
    "no"    : 0,
}

if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("用法: 把要转换的 JPG/PNG/BMP 文件拖到.exe图标上即可")
    #     time.sleep(3)
    #     sys.exit(0)
    cf = Converter.FLAG.CF_ALPHA_2_BIT
    out_c = 0
    out_bin = 0
    path = "images"

    f = open("config", 'r+')
    cf_data = f.read()
    print(cf_data)
    cf_data = cf_data.replace(" ", "")
    for data in cf_data.split():
        name,value = data.split('=')
        if (name == "color_format"):
            cf = color_format_dir[value]
        if (name == "out_c"):
            out_c = cfg_en[value]
        if (name == "out_bin"):
            out_bin = cfg_en[value]
        if (path == "path"):
            out_bin = value
    f.close()

    print("\n")
    print("config list")
    print("cf=" + str(cf))
    print("out_c=" + str(out_c))
    print("out_bin=" + str(out_bin))
    print("path=" + path)
    print("\n")
    
    print("===========================================================")
    cnt = 1
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            continue

        if os.path.splitext(file_path)[1]== '.c' \
            or os.path.splitext(file_path)[1]== '.bin' \
            or os.path.splitext(file_path)[1]== '.h' \
            or file == '.gitignore' :
            continue

        print(file_path)
        print("converting...")
        c = Converter(path=file_path, dith=True, cf=cf)
        c.convert(cf)
        print("saving...")
        if(out_bin == 1):
            c.get_bin_file() # get and save data to files
        if(out_c == 1):
            c.get_c_code_file() # get and save data to files
        
        print("file {} done\n".format(cnt))
        cnt = cnt + 1
    
    print("\nPlease input anything to exit")
    msvcrt.getch()


