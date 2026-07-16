import os


FONTS_DIR = "fonts"

os.makedirs(
    FONTS_DIR,
    exist_ok=True
)


def save_font(file_name, data):

    if not file_name.lower().endswith(
        (".ttf", ".otf")
    ):
        return None

    path = os.path.join(
        FONTS_DIR,
        file_name
    )

    with open(
        path,
        "wb"
    ) as f:
        f.write(data)

    return path



def get_fonts():

    fonts = []

    for file in os.listdir(FONTS_DIR):

        if file.lower().endswith(
            (".ttf", ".otf")
        ):
            fonts.append(file)

    return fonts



def delete_font(font_name):

    path = os.path.join(
        FONTS_DIR,
        font_name
    )

    if os.path.exists(path):

        os.remove(path)

        return True

    return False



def font_exists(font_name):

    path = os.path.join(
        FONTS_DIR,
        font_name
    )

    return os.path.exists(path)