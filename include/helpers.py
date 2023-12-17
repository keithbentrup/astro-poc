import debugpy

def start_debug():
  debugpy.listen(("0.0.0.0", 5678))
  debugpy.wait_for_client()
  debugpy.breakpoint()
