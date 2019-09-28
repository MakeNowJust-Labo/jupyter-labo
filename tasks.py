from invoke import Collection, task
import os

import setup

JUPYTER_CONFIG = f"{os.getcwd()}/.jupyter/jupyter_notebook_config.py"
JUPYTER_NOTEBOOK_DIR = f"{os.getcwd()}"

@task
def jupyter(c):
    c.run(f"""
        jupyter lab                               \\
            --config {JUPYTER_CONFIG}             \\
            --notebook-dir {JUPYTER_NOTEBOOK_DIR}
    """)

namespace = Collection(setup, jupyter)
