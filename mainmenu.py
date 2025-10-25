from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()

def main_menu():
    table = Table(title="Phantom_toolbox", box=box.ROUNDED)
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Description", style="magenta")

    table.add_row("1", "Reconnaissance Tools")
    table.add_row("2", "Exploitation Tools")
    table.add_row("3", "Reporting & Logs")
    table.add_row("4", "Update Toolbox")
    table.add_row("5", "Exit")
    console.print(Panel(table, title="[bold green]Main Menu[/]", subtitle="Select an option (type 'help' for info)", border_style="blue"))

def get_choice():
    return Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "help", "exit"], default="1")

def main():
    console.clear()
    main_menu()
    choice = get_choice()
    if choice == "help":
        console.print(Panel("[bold magenta]Help:[/]\nChoose a menu option by number. Type 'exit' to quit.", border_style="magenta"))
    elif choice == "1":
        console.print(Panel("[cyan]Reconnaissance Tools selected![/]", border_style="cyan"))
    # ... handle other choices

if __name__ == "__main__":
    main()