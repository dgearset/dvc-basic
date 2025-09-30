import dvc.api

with dvc.api.open(
    "data/data.xml",
    repo="https://github.com/dgearset/dvc-basic.git",
    rev="main"   # optional: specify branch, tag, or commit
) as fd:
    data = fd.read()
    print(data) 
