import subprocess
from addons.gui import Procedure
from utils.os_commands import openServerConsole

class CustomProcedure(Procedure):
    id = 3
    name = "OPEN [orange4]CS:GO[/orange4] Server Console"
    description= "( [bold underline]CTRL + A + D to detach[/bold underline] )"

    def run():
        openServerConsole()
        return