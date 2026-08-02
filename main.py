"""
main.py — AMTCE Root Entrypoint Wrapper
=======================================
Delegates execution directly to `simpler update/main.py` so there is only ONE
single implementation to maintain across the codebase.
"""

import os
import sys
import runpy

_REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
_SIMPLER_UPDATE_ROOT = os.path.join(_REPO_ROOT, "simpler update")

if _SIMPLER_UPDATE_ROOT not in sys.path:
    sys.path.insert(0, _SIMPLER_UPDATE_ROOT)
if _REPO_ROOT not in sys.path:
    sys.path.append(_REPO_ROOT)

if __name__ == "__main__":
    target_script = os.path.join(_SIMPLER_UPDATE_ROOT, "main.py")
    runpy.run_path(target_script, run_name="__main__")
