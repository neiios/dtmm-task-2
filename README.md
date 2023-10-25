# dtmm-task-2

enjoy :)

to run the project install python 3.11, create a virtual env, enter it and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

after that run this command inside the git repo

```bash
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'
```

## conclusions

never ever ever use jupyter notebooks for anything. never.
