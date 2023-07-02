from os import path
from dotenv import dotenv_values

_env = dotenv_values()

OPENAI_API_KEY = _env["OPENAI_API_KEY"]


_dsl_dir = (
    path.dirname(
        path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
    )
    + "/data/inputs_gen/dsl/"
)

DSL_PROMPT_1_INTRO_MD = _dsl_dir + "dsl_prompt_1_intro.md"
DSL_PROMPT_2_EXAMPLES_INTRO_MD = _dsl_dir + "dsl_prompt_2_examples_intro.md"
DSL_PROMPT_3_NOW_MD = _dsl_dir + "dsl_prompt_3_now.md"

DSL_PY = _dsl_dir + "dsl.py"

QUESTION_0_MD = _dsl_dir + "question_0.md"
DSL_0_PY = _dsl_dir + "dsl_0.py"

QUESTION_1_MD = _dsl_dir + "question_1.md"
DSL_1_PY = _dsl_dir + "dsl_1.py"

QUESTION_2_MD = _dsl_dir + "question_2.md"
DSL_2_PY = _dsl_dir + "dsl_2.py"


with open(DSL_PROMPT_1_INTRO_MD, "r") as f:
    DSL_PROMPT_1_INTRO = f.read()

with open(DSL_PROMPT_2_EXAMPLES_INTRO_MD, "r") as f:
    DSL_PROMPT_2_EXAMPLES_INTRO = f.read()

with open(DSL_PROMPT_3_NOW_MD, "r") as f:
    DSL_PROMPT_3_NOW = f.read()

with open(DSL_PY, "r") as f:
    DSL = f.read()

with open(QUESTION_0_MD, "r") as f:
    QUESTION_0 = f.read()

with open(DSL_0_PY, "r") as f:
    DSL_0 = f.read()

with open(QUESTION_1_MD, "r") as f:
    QUESTION_1 = f.read()

with open(DSL_1_PY, "r") as f:
    DSL_1 = f.read()

with open(QUESTION_2_MD, "r") as f:
    QUESTION_2 = f.read()

with open(DSL_2_PY, "r") as f:
    DSL_2 = f.read()


SYSTEM_TEMPLATE = f"""
{DSL_PROMPT_1_INTRO}

```python
{DSL}
```

{DSL_PROMPT_2_EXAMPLES_INTRO}

Example 1:

```md
{QUESTION_0}
```

```python
{DSL_0}
```

Example 2:

```md
{QUESTION_1}
```

```python
{DSL_1}
```
"""

HUMAN_TEMPLATE = f"""
{DSL_PROMPT_3_NOW}

```md
{{question}}
```
"""
