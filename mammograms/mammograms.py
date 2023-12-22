from pathlib import Path
from typing import Dict, Final, Iterator, List


CASES_DIR: Final[Path] = Path(__file__).parent / "cases"
STANDARD_VIEWS: Final[List[str]] = ["rcc", "lcc", "rmlo", "lmlo"]
CASES: Final[List[Dict[str, Path]]] = [
    {v: CASES_DIR / "sfm-benign-0" / f"{p}.dcm" for v, p in zip(STANDARD_VIEWS, ["1-132", "1-130", "1-133", "1-131"])},
    {v: CASES_DIR / "sfm-malign-0" / f"{p}.dcm" for v, p in zip(STANDARD_VIEWS, ["1-282", "1-280", "1-283", "1-281"])},
]


def gen_cases() -> Iterator[Dict[str, Path]]:
    # If additional cases are needed, perhaps we can retrieve them as needed from somewhere else
    for mammo_case in CASES:
        yield mammo_case
