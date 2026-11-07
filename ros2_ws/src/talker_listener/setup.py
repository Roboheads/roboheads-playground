from setuptools import setup

setup(
    name='talker_listener',
    version='0.1.0',
    packages=['talker_listener'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/talker_listener']),
        ('share/talker_listener', ['package.xml']),
    ],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'talker = talker_listener.talker:main',
            'listener = talker_listener.listener:main',
        ],
    },
)
