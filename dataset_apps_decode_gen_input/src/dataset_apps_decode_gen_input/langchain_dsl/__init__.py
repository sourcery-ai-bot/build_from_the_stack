from os import path
from dotenv import dotenv_values

_env = dotenv_values()

OPENAI_API_KEY = _env["OPENAI_API_KEY"]


_dsl_dir = f"{path.dirname(path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__))))))}/data/inputs_gen/dsl/"

DSL_PROMPT_1_INTRO_MD = f"{_dsl_dir}dsl_prompt_1_intro.md"
DSL_PROMPT_2_EXAMPLES_INTRO_MD = f"{_dsl_dir}dsl_prompt_2_examples_intro.md"
DSL_PROMPT_3_NOW_MD = f"{_dsl_dir}dsl_prompt_3_now.md"

DSL_PY = f"{_dsl_dir}dsl_declare.py"

QUESTION_0_MD = f"{_dsl_dir}question_0.md"
DSL_0_PY = f"{_dsl_dir}dsl_0.py"

QUESTION_1_MD = f"{_dsl_dir}question_1.md"
DSL_1_PY = f"{_dsl_dir}dsl_1.py"

QUESTION_2_MD = f"{_dsl_dir}question_2.md"
DSL_2_PY = f"{_dsl_dir}dsl_2.py"


with open(DSL_PROMPT_1_INTRO_MD, "r", encoding="utf-8") as f:
    DSL_PROMPT_1_INTRO = f.read()

with open(DSL_PROMPT_2_EXAMPLES_INTRO_MD, "r", encoding="utf-8") as f:
    DSL_PROMPT_2_EXAMPLES_INTRO = f.read()

with open(DSL_PROMPT_3_NOW_MD, "r", encoding="utf-8") as f:
    DSL_PROMPT_3_NOW = f.read()

with open(DSL_PY, "r", encoding="utf-8") as f:
    DSL = f.read()

with open(QUESTION_0_MD, "r", encoding="utf-8") as f:
    QUESTION_0 = f.read()

GENERATE_INPUT_MARKER = "GENERATE_INPUT"
with open(DSL_0_PY, "r", encoding="utf-8") as f:
    content = f.read()
    DSL_0 = content.split(GENERATE_INPUT_MARKER)[-1]

with open(QUESTION_1_MD, "r", encoding="utf-8") as f:
    QUESTION_1 = f.read()

with open(DSL_1_PY, "r", encoding="utf-8") as f:
    content = f.read()
    DSL_1 = content.split(GENERATE_INPUT_MARKER)[-1]

with open(QUESTION_2_MD, "r", encoding="utf-8") as f:
    QUESTION_2 = f.read()

with open(DSL_2_PY, "r", encoding="utf-8") as f:
    content = f.read()
    DSL_2 = content.split(GENERATE_INPUT_MARKER)[-1]


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
{QUESTION_2}
```

```python
{DSL_2}
```
"""

HUMAN_TEMPLATE = f"""
{DSL_PROMPT_3_NOW}

```md
{{question}}
```
"""
