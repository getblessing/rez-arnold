
import os


name = "arnold_sdk"

version = os.path.basename(os.getcwd())

requires = [
    "arnold_core-%s" % version,
]

variants = [
    ["platform-*"]
]

private_build_requires = ["rezutil-1"]
build_command = "python -m rezutil build {root} --use-zip"


def commands():
    env = globals()["env"]

    env.ARNOLD_LOCATION = "{root}"
