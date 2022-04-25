from colorama import Fore
import platform
import sys
import ctypes
from i import Variables

lib = ctypes.windll.kernel32

t = lib.GetTickCount64()

t = int(str(t)[:-3])

mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

reset = Fore.RESET

ascii = rf'''
{Fore.CYAN}  ___  ___      {Fore.RED + Variables.User + Fore.MAGENTA + "@" + Fore.GREEN + platform.system() + reset + Fore.GREEN}
{Fore.CYAN} / __|/ _ \     {Fore.YELLOW + "CPU: " + reset + Variables.CPU}
{Fore.CYAN} \__ \  __/     {Fore.YELLOW +"System: " + reset + platform.system()}
{Fore.CYAN} |___/\___|     {Fore.YELLOW +"Ram: " + reset + Variables.ram}
{Fore.LIGHTYELLOW_EX}     ___        {Fore.GREEN +"Terminal: " + reset + Variables.term}
{Fore.LIGHTYELLOW_EX}    / _ \       {Fore.GREEN +"Uptime: " + reset + f"{days} days, {hour:02}:{mins:02}:{sec:02}"}
{Fore.CYAN}   | | | |
{Fore.CYAN}   | |_| |      {Fore.BLACK +"███" + reset}{Fore.RED +"███" + reset}{Fore.GREEN +"███" + reset}{Fore.YELLOW +"███" + reset}{Fore.BLUE +"███" + reset}{Fore.MAGENTA +"███" + reset}{Fore.CYAN +"███" + reset}{Fore.WHITE +"███" + reset}
{Fore.LIGHTYELLOW_EX}    \___/       {Fore.LIGHTBLACK_EX +"███" + reset}{Fore.LIGHTRED_EX +"███" + reset}{Fore.LIGHTGREEN_EX +"███" + reset}{Fore.LIGHTYELLOW_EX +"███" + reset}{Fore.LIGHTBLUE_EX +"███" + reset}{Fore.LIGHTMAGENTA_EX +"███" + reset}{Fore.LIGHTCYAN_EX +"███"+ reset}{Fore.LIGHTWHITE_EX +"███"+ reset}
'''

print(ascii)
