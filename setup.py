from subprocess import check_output
from setuptools import setup


def get_version():
    # https://github.com/uc-cdis/dictionaryutils/pull/37#discussion_r257898408
    try:
        tag = check_output(
            ["git", "describe", "--tags", "--abbrev=0", "--match=[0-9]*"]
        )
        return tag.decode("utf-8").strip("\n")
    except Exception:
        raise RuntimeError(
            "The version number cannot be extracted from git tag in this source "
            "distribution; please either download the source from PyPI, or check out "
            "from GitHub and make sure that the git CLI is available."
        )


setup(
    name="psqlgraph",
    version=get_version(),
    packages=["psqlgraph"],
    install_requires=[
        "psycopg2-binary~=2.8",
        "sqlalchemy~=1.3",
        "py2neo~=2.0",
        "progressbar",
        "avro~=1.7",
        "xlocal~=0.5",
        "requests~=2.5",
        "six>=1.12.0",
    ],
)
