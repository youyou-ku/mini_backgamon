from setuptools import setup, find_packages

setup(
    name='mini-backgamon',
    version="0.0.1",
    description='Mini Back Gamon Program.',
    author='youyou-ku',
    url='https://github.com/youyou-ku/mini_backgamon.git',
    author_email='murata.yu.86r@st.kyoto-u.ac.jp',
    install_requires=["random"],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)