from colorama import Fore
import platform
import sys
import ctypes
from osinfo import Variables

lib = ctypes.windll.kernel32

t = lib.GetTickCount64()

t = int(str(t)[:-3])
balloon = '\U0001F388'
rocket = '\U0001F680'
ufo = '\U0001F6F8'
fire = '\U0001F525'
planet = '\U0001FA90'
time = '\U0001F319'
color1 = '\U0001F3B2'
color2 = '\U0001F9E9'
mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

reset = Fore.RESET

ascii = rf'''
{Fore.CYAN}  ___  ___      {balloon} {Fore.RED + Variables.User + Fore.MAGENTA + "@" + Fore.GREEN + platform.system() + reset + Fore.GREEN}
{Fore.CYAN} / __|/ _ \     {rocket} {Fore.YELLOW + "CPU: " + reset + Variables.CPU}
{Fore.CYAN} \__ \  __/     {ufo} {Fore.YELLOW +"System: " + reset + platform.system()}
{Fore.CYAN} |___/\___|     {fire} {Fore.YELLOW +"Ram: " + reset + Variables.ram}
{Fore.LIGHTYELLOW_EX}     ___        {planet} {Fore.GREEN +"Terminal: " + reset + Variables.term}
{Fore.LIGHTYELLOW_EX}    / _ \       {time} {Fore.GREEN +"Uptime: " + reset + f"{days} days, {hour:02}:{mins:02}:{sec:02}"}
{Fore.CYAN}   | | | |
{Fore.CYAN}   | |_| |      {color1} {Fore.BLACK +"███" + reset}{Fore.RED +"███" + reset}{Fore.GREEN +"███" + reset}{Fore.YELLOW +"███" + reset}{Fore.BLUE +"███" + reset}{Fore.MAGENTA +"███" + reset}{Fore.CYAN +"███" + reset}{Fore.WHITE +"███" + reset}
{Fore.LIGHTYELLOW_EX}    \___/       {color2} {Fore.LIGHTBLACK_EX +"███" + reset}{Fore.LIGHTRED_EX +"███" + reset}{Fore.LIGHTGREEN_EX +"███" + reset}{Fore.LIGHTYELLOW_EX +"███" + reset}{Fore.LIGHTBLUE_EX +"███" + reset}{Fore.LIGHTMAGENTA_EX +"███" + reset}{Fore.LIGHTCYAN_EX +"███"+ reset}{Fore.LIGHTWHITE_EX +"███"+ reset}
'''

print(ascii)
