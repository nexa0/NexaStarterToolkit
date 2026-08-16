from colorama import Fore, Style, init
from core.banner import show_banner
from core.utils import clear, pause, safe_input
from tools.hash_checker import run as hash_checker
from tools.file_hasher import run as file_hasher
from tools.password_strength import run as password_strength
from tools.base64_tool import run as base64_tool
from tools.ip_info import run as ip_info
from tools.http_status import run as http_status
from tools.port_checker import run as port_checker
from tools.metadata_viewer import run as metadata_viewer

init(autoreset=True)

TOOLS = {
    "1": ("Hash Checker", hash_checker),
    "2": ("File Hasher", file_hasher),
    "3": ("Password Strength", password_strength),
    "4": ("Base64 Tool", base64_tool),
    "5": ("IP Information", ip_info),
    "6": ("HTTP Status", http_status),
    "7": ("Port Checker", port_checker),
    "8": ("Metadata Viewer", metadata_viewer),
}

def menu():
    clear()
    show_banner()
    print(Fore.CYAN + "  Security • Network • Utility Tools")
    print(Fore.WHITE + "  " + "─" * 52)
    for key, (name, _) in TOOLS.items():
        print(f"  {Fore.YELLOW}[{key}]{Style.RESET_ALL} {name}")
    print(f"  {Fore.RED}[0]{Style.RESET_ALL} Exit")
    print()

def main():
    while True:
        menu()
        choice = safe_input(f"{Fore.CYAN}NEXA {Fore.WHITE}>{Style.RESET_ALL} ").strip()
        if choice == "0":
            print(f"\n{Fore.GREEN}[+] Thanks for using Nexa Basic Toolkit.{Style.RESET_ALL}")
            break
        if choice in TOOLS:
            clear()
            show_banner()
            name, tool = TOOLS[choice]
            print(f"{Fore.CYAN}[*] {name}{Style.RESET_ALL}\n")
            try:
                tool()
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}[!] Operation cancelled.{Style.RESET_ALL}")
            except Exception as exc:
                print(f"\n{Fore.RED}[!] Error: {exc}{Style.RESET_ALL}")
            pause()
        else:
            print(f"{Fore.RED}[!] Invalid option.{Style.RESET_ALL}")
            pause()

if __name__ == "__main__":
    main()
