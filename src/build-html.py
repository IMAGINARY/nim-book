import sys
from yattag import Doc


def build():
    doc, tag, text, line = Doc().ttl()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis('<link href="css/default.css" rel="stylesheet">')
        with tag('body'):
            for a in range(9, -1, -1):
                for b in range(9, -1, -1):
                    with tag('article', id=f'page-{a}-{b}', klass='even' if ((a * 10 + b) % 2 == 1) else 'odd'):
                        line('h2', f'{a}-{b}')
                        for c in range(9, -1, -1):
                            with tag('div', klass='state', id=f'state-{a}-{b}-{c}'):
                                doc.stag('img', src=f'img/states/{a}-{b}-{c}.svg')

    return doc.getvalue()


if __name__ == '__main__':
    output = build()
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'w') as outfile:
            outfile.write(output)
    else:
        print(output)
