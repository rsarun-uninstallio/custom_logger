from distutils.core import setup
setup(
  name = 'custom_logger',
  packages = ['custom_logger'],
  version = '0.1',
  license='MIT',
  description = 'CustomLogger - CustomLogger',
  author = 'arun.rs',
  author_email = 'arunrs@uninstall.io',
  url = 'https://github.com/rsarun-uninstallio/custom_logger',
  download_url = 'https://github.com/rsarun-uninstallio/customlogger/archive/v0.1.tar.gz',
  keywords = ['logging', 'customlogger'],
  install_requires=['logging', 'apprequest'],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
  ],
)