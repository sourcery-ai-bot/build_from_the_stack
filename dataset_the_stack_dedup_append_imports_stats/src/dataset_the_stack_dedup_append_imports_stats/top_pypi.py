# Stdlib imports
import json

# Project imports
from ._config import TOP_PYPI_PACKAGES_JSON


# Read JSON
with open(TOP_PYPI_PACKAGES_JSON, "r") as f:
    top_pypi_packages_json = json.load(f)

top_pypi_packages = {row["project"] for row in top_pypi_packages_json["rows"]}
