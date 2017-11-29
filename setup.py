#!/usr/bin/env python3
# =============================================================================
# @file    setup.py
# @brief   Nostril setup file
# @author  Michael Hucka <mhucka@caltech.edu>
# @license Please see the file named LICENSE in the project directory
# @website https://github.com/casics/nostril
# =============================================================================

import os
from   setuptools import setup, find_packages
import sys
import nostril

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    reqs = f.read().rstrip().splitlines()

setup(
    name=nostril.__version__.__title__,
    version=nostril.__version__.__version__,
    url=nostril.__version__.__url__,
    author=nostril.__version__.__author__,
    author_email=nostril.__version__.__email__,
    license=nostril.__version__.__license__,
    description='Nostril (Nonsense String Evaluator) implements a heuristic mechanism to infer whether a given word or text string is likely to be meaningful or nonsense.',
    keywords="program-analysis text-processing machine-learning",
    packages=['nostril'],
    packages_dir={'nostril': 'nostril'},
    package_data={'nostril': ['docs/*.md', 'LICENSE', 'requirements.txt']},
    install_requires=reqs,
    include_package_data=True,
    platforms='any',
)