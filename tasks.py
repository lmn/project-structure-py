#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

import glob
from invoke import task


# --------------------------------------------------------------------------- #
# Settings
# --------------------------------------------------------------------------- #

PACKAGE_NAME = "package"
DEPENDENCIES = "deps.txt"

# --------------------------------------------------------------------------- #
# App Tasks
# --------------------------------------------------------------------------- #

@task
def play(ctx, mode='development'):
    """ Start Application """
    from package import app
    from package.loader import config
    from bottle import run

    if mode in config['api']:
        print(f"Starting with {config['api'][mode]}")

        # https://docs.python.org/3/library/tracemalloc.html
        if mode == 'development':
            import tracemalloc
            tracemalloc.start()

        # Start App
        run(app, **config['api'][mode])

    # Default Message
    else:
        print(f"Please verify {mode} under config.yml")

# --------------------------------------------------------------------------- #
# Tasks
# --------------------------------------------------------------------------- #

@task
def deps(ctx):
    """ Install Dependencies """
    print("Installing Dependencies")
    ctx.run(f"pip3 install -r {DEPENDENCIES}")

@task
def docs(ctx):
    """ Documentation Live Server"""
    print("Start Doc Server")
    ctx.run(f"pdoc --http : {PACKAGE_NAME}")

@task
def docs_build(ctx):
    """ Documentation Build Static """
    print("Start Doc Server")
    ctx.run(f"pdoc --http : {PACKAGE_NAME}")

@task
def lint(ctx):
    """ Run PyLint """
    files = glob.glob('*/**.py')
    ctx.run("pylint {}".format(' '.join(files)))

@task
def lint(ctx):
    """ Run Unit Test """
    files = glob.glob('*/**.py')
    ctx.run("pylint {}".format(' '.join(files)))

@task
def bump(ctx):
    """ Version Bumper """
    branch = ctx.run("git rev-parse --abbrev-ref HEAD")
    if branch is "master":
        ctx.run("bumpversion minor")
    elif branch is "develop":
        ctx.run("bumpversion patch")
    elif branch is "release":
        ctx.run("bumpversion major")

# --------------------------------------------------------------------------- #
# END
# --------------------------------------------------------------------------- #

# EOF
