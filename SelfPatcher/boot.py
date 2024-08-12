try:
    from .plugin import *
except ImportError:
    print("[SelfPatcher][INFO] The current platform-arch is unsupported.")
