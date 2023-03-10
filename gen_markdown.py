#!/usr/bin/python3
"""
Generate Markdown from ../fixtures product test data
"""

import json
import os
from pathlib import Path

FIXTURES_MARKDOWN = Path(__file__).with_name("FIXTURES.md")
FIXTR = Path(__file__).parent / "fixtures"


def gen_markdown():
    """gen_markdown"""
    mdstrs = {}
    for dirpath, dirnames, filenames in os.walk(FIXTR):
        if len(dirnames) == 0:
            for filename in filenames:
                if filename.endswith(".json"):
                    file = Path(dirpath).joinpath(filename)
                    with file.open("r", encoding="utf-8") as jptr:
                        jobj = json.load(jptr)
                        plugin = Path(dirpath).name
                        mdstrs[plugin] = json.dumps(jobj, indent=4)

    with FIXTURES_MARKDOWN.open("w", encoding="utf-8") as fptr:
        fptr.write("# Fixtures\n\n")
        for key, val in mdstrs.items():
            fptr.write(f"## Plugin: `{key}`")
            fptr.write("\n\n\n")
            fptr.write(f"```\n{val}\n```")
            fptr.write("\n\n\n")


if __name__ == "__main__":
    gen_markdown()
