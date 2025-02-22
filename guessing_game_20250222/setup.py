from setuptools import setup

setup(name='guessing_game_20250222', 
      version='0.1.0', 
      packages=['guessing_game_20250222'],
      author = 'fmcgh',
      entry_points={
          'console_scripts': [
              'guessing-game=guessing_game_20250222.cli:main',
        ],
      },
      author_email = 'fmcgh@github.user',
      zip_safe=False)
