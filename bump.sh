cd /Users/pcotton/github/helicopter/
rm /Users/pcotton/github/helicopter/dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
