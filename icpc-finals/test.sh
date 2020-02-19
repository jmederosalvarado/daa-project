#!/bin/zsh

pyversion=pypy3-72

pyfile=$1
pyfolder=${pyfile%%/*}
pyname=${${pyfile%%.py}##*/}

pypy -m py_compile $pyfile

for file in $(ls $2/*.in); do
    test=${${file%%.in}##*/}
    echo $test
    pypy $pyfolder/__pycache__/$pyname.$pyversion.pyc < $2/$test.in | diff - $2/$test.ans
done