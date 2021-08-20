rm -r dist/ &> /dev/null

python -m build
python -m twine upload  dist/*