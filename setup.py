import setuptools
import versioneer 

if __name__ == "__main__":
    setuptools.setup(
        name='sssdevops',
        version='2.0',
        description='Example project for the SSS Devops course',
        author='Amulya K. Pervaje',
        url="https://github.com/amilumas/sssdevops.git",
        license='BSD 3-C',
        packages=setuptools.find_packages(),
        install_requires=[
            'jsonschema',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest>=3.0',
		'pytest-cov'
            ],
        },

        tests_require=[
            'pytest',
        ],
        zip_safe=True,
    )
