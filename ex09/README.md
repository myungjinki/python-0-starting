# https://packaging.python.org/en/latest/tutorials/packaging-projects/

```
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

# https://pip.pypa.io/en/stable/cli/pip_show/
# https://toml.io/en/
# https://packaging.python.org/en/latest/specifications/declaring-project-metadata/
# https://github.com/pypa/packaging-problems/issues/645
# https://stackoverflow.com/questions/75570780/pip-show-does-not-show-summary-home-page-author-and-license
# https://stackoverflow.com/questions/16385099/why-does-pip-convert-underscores-to-dashes
# https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
# https://devocean.sk.com/blog/techBoardDetail.do?ID=164866&boardType=techBlog
# https://github.com/pypa/hatch

# Why setuptools change name underscore to dash?
# https://github.com/pypa/setuptools/issues/2522


```
python -m build && pip install ./dist/ft_package-0.0.1.tar.gz && pip show -v ft_package
```