import typer
from addons.gui import Procedure
from rich.prompt import Prompt
from utils.os_commands import stopCSGOServer, verifyCSGOServerInstallation


class CustomProcedure(Procedure):
    id=7
    name= "Stop [orange4]CS:GO[/orange4] Server"
    description = ""

    def run():
        if not verifyCSGOServerInstallation():
            print('CSGO is not installed, please install it first.')
            return
        
        stopCSGOServer()
        print('CS:GO Server stopped.. Please visit console to see updates.')

        pass