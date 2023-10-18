# dtmm-task-2

enjoy :)

To run the project create a virtual env, enter it and install dependencies:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After that run this command inside the git repo:

```bash
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'
```
