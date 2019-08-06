### 同步 README.md 内容到 README.rst
pandoc -o README.rst README.md

### 打包
python setup.py sdist bdist_wheel

### 发布
twine upload dist/*