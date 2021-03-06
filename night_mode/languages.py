import gettext
from os import path

from anki.lang import getLang, _ as fallback_translation

lang = getLang()
this_dir = path.dirname(path.abspath(__file__))
locale_dir = path.join(this_dir, 'locale')
trans = gettext.translation('Anki-Night-Mode', locale_dir, languages=[lang], fallback=True)


def _(text):
    try:
        return trans.gettext(text)
    except Exception as e:
        print(e)
        return fallback_translation(text)
