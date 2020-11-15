from platform import system
from subprocess import run
from re import findall

def get_disks():
    """
        Returns a list of all mounted disks (for Windows platforms)

        >> ["A:", "B:", "C:"]
    """

    if system() != "Windows":
        raise OSError("For use with Windows platforms.")

    logicaldisks=run(
        ["wmic", "logicaldisk", "get", "name"],
        capture_output=True
    )

    return [disk for disk in findall("[A-Z]:", str(logicaldisks.stdout))]
