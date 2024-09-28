try:
    from .plugin import *
except ImportError as e:
    print(f"[SelfPatcher][INFO] The current platform-arch is unsupported: {e}")
