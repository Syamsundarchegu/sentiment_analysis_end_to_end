from setuptools import setup, find_packages

requirements = []

def get_requirments_file(filename:str):
    with open(filename,'r') as f:
        for line in f.readlines():
            requirements.append(line.replace('\n',""))
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements


setup(
    name="text_sentiment_analysis",
    author="syamsundar chegu",
    author_email="chegusyam396@gmail.com",
    version="0.0.1",
    requirements= get_requirments_file("requirements.txt"),
    packages = find_packages()
)
            