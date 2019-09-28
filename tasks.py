from invoke import task
import os

JUPYTER_CONFIG = f"{os.getcwd()}/.jupyter/jupyter_notebook_config.py"
JUPYTER_NOTEBOOK_DIR = f"{os.getcwd()}/notebook"

@task
def jupyter(c):
    c.run(f"""
      jupyter notebook                        \\
        --config {JUPYTER_CONFIG}             \\
        --notebook-dir {JUPYTER_NOTEBOOK_DIR}
    """)

@task
def setup_wolfram(c):
    with c.cd("deps/wolfram"):
        c.run("wolframscript -f configure-jupyter.wls remove")
        c.run("wolframscript -f configure-jupyter.wls add")
