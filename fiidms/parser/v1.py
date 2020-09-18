
# FORMAT
# ARTIST|ALBUM|TITLE|YOUTUBE_ID


# EXAMPLE FILE
# =v1
# Surprise|The realization|As it rolls|dQw4w9WgXcQ
# Reol|SIGMA|宵々古今 /YoiYoi Kokon|8IK6eLTNV1k

VERSION_TOKEN = "v1"

def parse(line):
    base = dict(zip(
        ['artist', 'album', 'title', 'youtube_id'],
        line.split('|')))
    base['artist'] = base['artist'].split(',')
    return base;


def parser(data_string):
    lines = data_string.split('\n')

    if not lines[0][0] == '=':
        raise ValueError("incorrect file format.")

    version = lines[0][1:].strip()

    if not version == "v1":
        raise ValueError(
            f"playlist version {version} does not match parser version {VERSION_TOKEN}")

    return map(parse, lines[1:])

