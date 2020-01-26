# UsercountAmp
### written in Phyton 3.8.1 by Strolch

from setuptools import setup

setup(
    name='player_amp',
    version='0.2',
    license='MIT',
    description='a little tool written in phyton to count all the active users',
    author='Strolch',
    author_email='hello.circles@gmail.com',
    url="https://github.com/R0b95/player_amp",
    download_url='https://github.com/R0b95/player_amp/archive/2.0.tar.gz',
    keywords=['AMP', 'UserCount', 'ActiveUser', 'ActivePlayer'],
    packages=['player_amp', 'player_amp.api_functions'],
    entry_points="""
        [console_scripts] 
            player_amp = player_amp.main:main
            player_amp.debug = player_amp.debug:debug
            player_amp.setserver = player_amp.setserver:setserver
        """,
    install_requires="""
        appdirs
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
