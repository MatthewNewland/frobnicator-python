from setuptools import setup


setup(
        name="frobnicator",
        version="1.0",
        description="Frobnicates things",
        packages=['frobnicator'],
        package_data={'frobnicator': ['*.ui', '*.png']},
        data_files=[('share/applications', ['frobnicator.desktop']),
                    ('share/icons/hicolor/scalable/apps', ['frobnicator.png']),
                    ('share/frobnicator', ['frobnicator.ui'])],
        entry_points={'gui_scripts': ['frobnicator = frobnicator:main']}
)
