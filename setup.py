import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
__version__="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME ="pankajventure7"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "pankajcse107@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)

