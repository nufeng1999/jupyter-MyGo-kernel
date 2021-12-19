from setuptools import setup

setup(name='jupyter_MyGo_kernel',
      version='0.0.1',
      description='Minimalistic Go kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyGo-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyGo-kernel/tarball/0.0.1',
      packages=['jupyter_MyGo_kernel'],
      scripts=['jupyter_MyGo_kernel/install_MyGo_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'Go'],
      include_package_data=True
      )
