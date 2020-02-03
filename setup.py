from setuptools import setup

setup(name='scrabble',
      version='0.1',
      description='Play scrabble at the command line',
      url='http://git.mango.local/kmeteyard/scrabble',
      author='Kieran Meteyard',
      author_email='kmeteyard@mango-solutions.com',
      license='MIT',
      packages=['scrabble'],
      package_data={'scrabble': ['dictionary.txt']},
      include_package_data=True,
      zip_safe=False)