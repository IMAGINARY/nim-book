import os
from invoke import task


@task
def build_state_images(c):
    outdir = os.path.abspath(os.path.relpath('build/html/img/states', os.path.dirname(__file__)))
    print(f'Building state images to {outdir}')
    c.run(f'poetry run python src/build-state-images.py {outdir}')


@task
def build_html(c):
    outpath = os.path.abspath(os.path.relpath('build/html/index.html', os.path.dirname(__file__)))
    print('Building HTML')
    c.run(f'poetry run python src/build-html.py {outpath}')


@task
def build_pdf(c):
    infile = os.path.abspath(os.path.relpath('build/html/index.html', os.path.dirname(__file__)))
    outfile = os.path.abspath(os.path.relpath('build/nim.pdf', os.path.dirname(__file__)))
    c.run(f'poetry run weasyprint {infile} {outfile}')


@task
def build_sample_image(c):
    outpath = os.path.abspath(os.path.relpath('build/sample.svg', os.path.dirname(__file__)))
    print(f'Building sample image to {outpath}')
    c.run(f'poetry run python src/build-sample-image.py {outpath}')


@task(build_state_images, build_html, build_pdf, default=True)
def build(c):
    pass


@task
def clean(c, html=True, state_images=True):
    patterns = ['build/nim.pdf', 'build/sample.svg']
    if html:
        patterns.append('build/html/index.html')
    if state_images:
        patterns.append('build/html/img/states/*.svg')
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))
