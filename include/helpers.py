import os

import debugpy


def start_debug():
  if os.environ.get("DEBUG_DAG") == "1":
    debugpy.listen(("0.0.0.0", 5678))
    debugpy.wait_for_client()
    debugpy.breakpoint()
