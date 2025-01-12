# Stdlib imports
from multiprocessing import Pool
from itertools import chain

# Third-party imports
import pandas as pd
from tqdm import tqdm
from datasets import load_from_disk, Dataset
from dataset_the_stack_dedup import TheStackDedup

# Project imports
from ._config import CACHE_DIR, NUM_PROC
from .analyze_imports_stats import (
    find_imports_stats,
    has_stdlib_imports,
    has_top_pypi_imports,
    has_other_imports,
)


class TheStackDedupAppendImportsStats:
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
        the_stack_dedup_ds = TheStackDedup().dataset()

        matches = the_stack_dedup_ds.map(
            lambda d: {
                "__imports_stats__": find_imports_stats(d["content"]),
            },
            num_proc=NUM_PROC,
        )

        return matches.map(
            lambda d: {
                "__has_stdlib_imports__": has_stdlib_imports(
                    d["__imports_stats__"]["ast.Import"],
                    d["__imports_stats__"]["ast.ImportFrom"],
                ),
                "__has_top_pypi_imports__": has_top_pypi_imports(
                    d["__imports_stats__"]["ast.Import"],
                    d["__imports_stats__"]["ast.ImportFrom"],
                ),
                "__has_other_imports__": has_other_imports(
                    d["__imports_stats__"]["ast.Import"],
                    d["__imports_stats__"]["ast.ImportFrom"],
                ),
            },
            num_proc=NUM_PROC,
        )
