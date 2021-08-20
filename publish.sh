if [[ "$1" != "test" ]] && [[ "$1" != "prod" ]]
then
    echo "unknown environment. use test or prod"
    exit
fi

rm -r dist/ &> /dev/null
python -m build

if [[ "$1" == "test" ]]
then 
    echo "publish to test.pypi"
    python -m twine upload --repository testpypi dist/*
    exit
fi

if [[ "$1" == "prod" ]]
then
    echo "publish to pypi"
    python -m twine upload dist/*
    exit
fi