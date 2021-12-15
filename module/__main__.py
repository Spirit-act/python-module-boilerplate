import os


def root_path() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("module was executed in standalone")
