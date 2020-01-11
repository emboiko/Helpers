from platform import system
from subprocess import run
from re import findall

def get_disks():
    """
        Returns all mounted disks
    """

    if system() != "Windows":
        raise OSError("For use with Windows platforms.")

    logicaldisks=run([
        "wmic",
        "logicaldisk",
        "get",
        "name"
    ], capture_output=True)

    disks=findall("[A-Z]:", str(logicaldisks.stdout))
    
    return [disk + "/" for disk in disks]
