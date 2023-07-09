# Third-party imports
from datasets import load_from_disk

# Project imports
from ._config import CACHE_DIR
from dataset_apps_decode_gen_input import APPSDecodeGenInput


DSL_GEN_BASE_DIR = "./data/inputs_gen/dsl/gen/"


class APPSDecodeGenInputRun:
    def __init__(self, *, logger):
        self._ds = None
        self.logger = logger

    def loads(self):
        try:
            ds = load_from_disk(CACHE_DIR)
            self.logger.info("Loaded dataset from cache")

        except FileNotFoundError:
            ds = self.build()
            ds.save_to_disk(CACHE_DIR)
            self.logger.info("Saved dataset to cache")

        self._ds = ds

    def dataset(self):
        if self._ds is None:
            self.loads()
        return self._ds

    def build(self):
        ds = APPSDecodeGenInput(
            logger=self.logger,
        ).dataset()

        for row in ds:
            generate_input_gpt_4 = self.process_dsl_py(row["solution: gpt-4"])
            generate_input_gpt_3 = self.process_dsl_py(row["solution: gpt-3.5-turbo"])

            file_name = f"dsl_{row['problem_id']}.py"

            with open(f"{DSL_GEN_BASE_DIR}/gpt-4/{file_name}", "w") as f:
                f.write(generate_input_gpt_4)

            with open(f"{DSL_GEN_BASE_DIR}/gpt-3.5-turbo/{file_name}", "w") as f:
                f.write(generate_input_gpt_3)

        return ds

    def process_dsl_py(self, dsl_py: str):
        stripped = dsl_py[10:-3]

        append = """\
from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


"""

        return append + stripped
