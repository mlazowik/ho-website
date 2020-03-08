import glob
from distutils.dir_util import copy_tree
import os
from pathlib import Path

import jinja2

script_dir = Path(os.path.dirname(__file__))

loader = jinja2.FileSystemLoader(script_dir / 'web')
env = jinja2.Environment(loader=loader)

PAGES = ['index', 'events', 'media', 'shop', 'about', 'contact']


def main():
    copy_tree(script_dir / 'web', str(script_dir / 'dist'))

    template = env.get_template('template.html.jinja2')
    for page in PAGES:
        with open(script_dir / 'web' / f'{page}-content.html', 'r') as content:
            with open(script_dir / 'dist' / f'{page}.html', 'w') as rendered:
                rendered.write(template.render(
                    content=content.read(),
                    page=page
                ))


if __name__ == '__main__':
    main()
