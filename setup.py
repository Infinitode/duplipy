from setuptools import setup, find_packages

setup(
    name='duplipy',
    version='0.1.6',
    author='Infinitode Pty Ltd',
    author_email='infinitode.ltd@gmail.com',
    description='A package for formatting and text replication.',
    long_description='DupliPy is a quick and easy-to-use package that can handle text formatting and data augmentation tasks for NLP in Python.',
    long_description_content_type='text/markdown',
    url='https://github.com/infinitode/duplipy',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'numpy',
        'langcodes',
        'joblib',
        'tqdm',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
)