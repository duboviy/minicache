from distutils.core import setup
setup(
  name = 'minicache',
  packages = ['minicache'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Python memory caching utilities.',
  author = 'Eugene Duboviy',
  author_email = 'eugene.dubovoy@gmail.com',
  url = 'https://github.com/duboviy/minicache', # use the URL to the github repo
  download_url = 'https://github.com/duboviy/minicache/tarball/0.0.1', # I'll explain this in a second
  keywords = ['cache', 'utility', 'optimization'], # arbitrary keywords
  classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  long_description="""
minicache extends existing caching utilities and provides a simple and pythonic way to cache values.
This project was created to suit the "memoization" needs, with a hook to turn it off (for testing or other purposes).
""",
  install_requires=[],
)
