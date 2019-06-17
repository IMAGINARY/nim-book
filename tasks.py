import os
from invoke import task

@task
def build_state_images(c):
    outdir = os.path.abspath(os.path.relpath('build/html/img/states', os.path.dirname(__file__)))
    print(f'Building state images to {outdir}')
    c.run(f'env/bin/python3 src/build-state-images.py {outdir}')

@task
def build_html(c):
    outpath = os.path.abspath(os.path.relpath('build/html/index.html', os.path.dirname(__file__)))
    print('Building HTML')
    c.run(f'env/bin/python3 src/build-html.py {outpath}')


@task
def build_pdf(c):
    infile = os.path.abspath(os.path.relpath('build/html/index.html', os.path.dirname(__file__)))
    outfile = os.path.abspath(os.path.relpath('build/nim.pdf', os.path.dirname(__file__)))
    c.run(f'env/bin/weasyprint {infile} {outfile}')

@task(build_state_images, build_html)
def build(c, state_images=False):
    c.run('env/bin/python3 --version')

@task
def path(c):
    print(os.path.dirname(__file__))

@task
def clean(c, html=False, state_images=False):
    patterns = ['build/nim.pdf']
    if html:
        patterns.append('build/html/index.html')
    if state_images:
        patterns.append('build/html/img/states')
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))