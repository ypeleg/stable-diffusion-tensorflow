

from setuptools import find_packages, setup

setup(name="stable_diffusion_tf_fixes",
      version="0.1",
      description="Stable Diffusion in Tensorflow / Keras",
      author="Yam Peleg",
      author_email='ypeleg2@gmail.com',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      url="https://github.com/ypeleg/stable-diffusion-tensorflow",
      packages=find_packages(),
      )