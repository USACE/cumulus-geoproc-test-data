#!/usr/bin/python3
"""
Generate Markdown from ../fixtures product test data
"""

import json
import os
from pathlib import Path


def gen_markdown():
    """gen_markdown"""
    mdstrs = {}
    readme = Path(__file__).with_name("README.md")
    fixtr = Path(__file__).parent / "fixtures"
    for dirpath, dirnames, filenames in os.walk(fixtr):
        if len(dirnames) == 0:
            for filename in filenames:
                if filename.endswith(".json"):
                    file = Path(dirpath).joinpath(filename)
                    with file.open("r", encoding="utf-8") as jptr:
                        jobj = json.load(jptr)
                        plugin = Path(dirpath).name
                        mdstrs[plugin] = json.dumps(jobj, indent=4)

    with readme.open("w", encoding="utf-8") as fptr:
        fptr.write("# Cumulus Geo-processor Test Data Sets\n\n# Fixtures\n\n")
        for key, val in mdstrs.items():
            fptr.write(f"## Plugin: `{key}`")
            fptr.write("\n\n\n")
            fptr.write(f"```\n{val}\n```")
            fptr.write("\n\n\n")


if __name__ == "__main__":
    gen_markdown()
