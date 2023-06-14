from distutils.core import setup


install_requires = [
    "requests",
    "beautifulsoup4>=4.11.2",

]
extras_require = {}
cpython_dependencies = [
    "PyDispatcher>=2.0.5",
]

def get_description():
    try:
      return open("README.rst", encoding="utf-8").read()
    except:
      return None
    
            
setup(
    name='omkar-temp-mail',
    packages=['omkar-temp-mail'],
    version='1.0.2',
    license='MIT',
    project_urls={
        "Documentation": "https://github.com/omkarcloud/omkar-temp-mail",
        "Source": "https://github.com/omkarcloud/omkar-temp-mail",
        "Tracker": "https://github.com/omkarcloud/omkar-temp-mail/issues",
    },

    description="Use Omkar Temporary for receiving temporary emails",
    long_description=get_description(),
    # long_description_content_type="text/markdown",
    author='Chetan Jain',
    author_email='chetan@omkar.cloud',
    maintainer="Chetan Jain",
    maintainer_email="chetan@omkar.cloud",

    keywords=["temp-mail","disposable-email","temporary-email","tempmail","temporary-email","disposable-email-addresses","python","mail-api","mail ","10minutemail","10minute","free-mail"],
    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
)