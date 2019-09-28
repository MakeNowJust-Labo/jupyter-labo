from invoke import task

SCALA_VERSION = "2.13.0"
ALMOND_VERSION = "0.8.1"

@task
def wolfram(c):
    with c.cd("deps/wolfram"):
        c.run("wolframscript -f configure-jupyter.wls remove")
        c.run("wolframscript -f configure-jupyter.wls add")

@task
def scala(c):
    c.run(f"""
        set -ex

        export SCALA_VERSION={SCALA_VERSION} ALMOND_VERSION={ALMOND_VERSION}

        rm -rf .cache/almond
        mkdir -p .cache/almond
        cd .cache/almond

        curl -Lo coursier https://git.io/coursier-cli
        chmod +x coursier
        ./coursier bootstrap \\
            -r jitpack \\
            -i user -I user:sh.almond:scala-kernel-api_$SCALA_VERSION:$ALMOND_VERSION \\
            sh.almond:scala-kernel_$SCALA_VERSION:$ALMOND_VERSION \\
            -o almond

        ./almond --force --install
    """)
