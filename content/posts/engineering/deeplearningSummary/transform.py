import os
import re

def transform_img(line):
    # 匹配img标签
    img_pattern = r'<img\s+src="(.*?)"\s*alt="(.*?)"\s*style="(.*?)"\s*/?>'
    match = re.search(img_pattern, line)
    if match:
        url, alt, style = match.groups()
        # 提取图片缩放比例
        zoom_pattern = r'zoom:\s*(\d+(?:\.\d+)?%?)\s*;?'
        zoom_match = re.search(zoom_pattern, style)
        if zoom_match:
            zoom = zoom_match.group(1)
            if not zoom.endswith('%'):
                zoom += '%'
        else:
            zoom = ''
        # 构造Markdown图片格式
        md_img = f'![{alt}]({url} "{zoom}")'
        return md_img
    else:
        return line

def transform_file(filename):
    try:
        dirname, name = os.path.split(filename)
        savepath = os.path.join(dirname, "transformed", name[:-3] + "-transformed" + name[-3:])
        os.makedirs(os.path.dirname(savepath), exist_ok=True)

        with open(filename, "r", encoding="utf-8") as r, open(savepath, "w", encoding="utf-8") as w:
            for line in r:
                w.write(transform_img(line))

    except Exception as e:
        print(f"Error transforming {filename}: {e}")

if __name__ == "__main__":
    filename = "wait_transform\zhuanhuan.md"
    transform_file(filename)