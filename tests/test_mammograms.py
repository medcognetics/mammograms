import re
from typing import Final

from test_mammograms.mammograms import *


TECH_ID: Final[str] = "tech"
MALIGN_ID: Final[str] = "malign"
NUM_ID: Final[str] = "num"
CASE_PATTERN: Final[re.Pattern] = re.compile(rf"(?P<{TECH_ID}>\S+)-(?P<{MALIGN_ID}>\S+)-(?P<{NUM_ID}>\S+)")


def test_exists() -> None:
    for mammo_case in gen_cases():
        for view, filename in mammo_case.items():
            assert view in STANDARD_VIEWS
            assert filename.exists()


def test_case_names() -> None:
    cases = list(CASES_DIR.iterdir())
    for mammo_case in cases:
        match = CASE_PATTERN.match(str(mammo_case.stem))
        assert match, f"`{mammo_case}` does not follow the expected naming convention."
        assert match.group(TECH_ID) == "sfm"  # In the future we could expand this to "ffdm" and "dbt"
        assert match.group(MALIGN_ID) in ["malign", "benign"]
        assert int(match.group(NUM_ID)) in list(range(len(cases)))
