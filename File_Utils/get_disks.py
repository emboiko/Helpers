from subprocess import run
from re import findall

def get_disks():
    """
        Returns all mounted disks
    """

    logicaldisks=run([
        "wmic",
        "logicaldisk",
        "get",
        "name"
    ], capture_output=True)

    disks=findall("[A-Z]:", str(logicaldisks.stdout))
    
    return [disk + "/" for disk in disks]
