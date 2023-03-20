#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from os import environ, name as nm
from sys import exit
from time import sleep

try:
    from censys.common.exceptions import (
        CensysAPIException,
        CensysException,
        CensysInvalidAPIKeyException,
        CensysRateLimitExceededException,
        CensysSearchAPIErrorException,
        CensysSearchAPITimeoutException,
        CensysSearchException,
        CensysUnauthorizedException,
    )
    from censys.search import CensysHosts
    from load_xl import read_config_file
    from rich.console import Console
    from rich.panel import Panel
except ImportError as e:
    print(f"Error: {e}")
    exit(1)


# Global Variables
console = Console()
get_os = str(nm).lower()


# Terminal Colors
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


if get_os == "nt":
    HEADER = ""
    OKBLUE = ""
    OKCYAN = ""
    OKGREEN = ""
    WARNING = ""
    FAIL = ""
    ENDC = ""
    BOLD = ""
    UNDERLINE = ""
else:
    HEADER = bcolors.HEADER
    OKBLUE = bcolors.OKBLUE
    OKCYAN = bcolors.OKCYAN
    OKGREEN = bcolors.OKGREEN
    WARNING = bcolors.WARNING
    FAIL = bcolors.FAIL
    ENDC = bcolors.ENDC
    BOLD = bcolors.BOLD
    UNDERLINE = bcolors.UNDERLINE


def banner():
    banner = f"""{OKCYAN}{BOLD}
       _..._                                                                     
    .-'_..._''.                                                                  
  .' .'      '.\     __.....__        _..._                   __.....__     .--. 
 / .'            .-''         '.    .'     '.             .-''         '.   |__| 
. '             /     .-''"'-.  `. .   .-.   .           /     .-''"'-.  `. .--. 
| |            /     /________\   \|  '   '  |          /     /________\   \|  | 
| |            |                  ||  |   |  |       _  |                  ||  | 
. '            \    .-------------'|  |   |  |     .' | \    .-------------'|  | 
 \ '.          .\    '-.____...---.|  |   |  |    .   | /\    '-.____...---.|  | 
  '. `._____.-'/ `.             .' |  |   |  |  .'.'| |// `.             .' |__| 
    `-.______ /    `''-...... -'   |  |   |  |.'.'.-'  /    `''-...... -'        
             `                     |  |   |  |.'   \_.'                          
                                   '--'   '--'                                 
         {HEADER}{BOLD}A Python script to search Censys.io for hosts and services using API.{ENDC}  
{ENDC}"""
    print(
        banner
        + "\n"
        + " " * 35
        + "By: @sc4rfurry\n"
        + " " * 35
        + "Version: 1.0.0\n"
        + " " * 35
        + "License: MIT\n"
        + " " * 35
        + "Github: https://github.com/sc4rfurry\n"
        + "-" * 160
        + "\n"
    )


def check_api_key():
    global api
    console.print(
        f"\n\n[cyan bold][+][/cyan bold] [dark_magenta bold]Checking API key...[/dark_magenta bold]"
    )
    sleep(1)
    try:
        read_config_file(".configx")
        if environ["API_ID"] == "" or environ["API_SECRET"] == "":
            print(f"\n{FAIL}Error: API_ID or API_SECRET not set.{ENDC}")
            exit(1)
        else:
            app_id = environ["API_ID"]
            app_secret = environ["API_SECRET"]
            console.print(
                f"[cyan bold][^][/cyan bold] [green bold]Found API_ID and API_SECRET...[/green bold]"
            )
            sleep(1)
            api = CensysHosts(app_id, app_secret)
            return api
    except (
        CensysAPIException,
        CensysException,
        CensysInvalidAPIKeyException,
        CensysRateLimitExceededException,
        CensysSearchAPIErrorException,
        CensysSearchAPITimeoutException,
        CensysSearchException,
        CensysUnauthorizedException,
    ) as e:
        print(f"Error: {e}")
        exit(1)
    except KeyError:
        console.print(f"{FAIL}Error: API_ID or API_SECRET not set.{ENDC}")
        exit(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except Exception as e:
        console.print("\nExiting...\n", style="bold red blink")
        exit(1)


def main(query):
    try:
        console.print(
            f"\n\n[cyan bold][+][/cyan bold] [orange_red1 bold]Searching for[/orange_red1 bold] [green_yellow bold]{query}[/green_yellow bold]"
        )
        results = api.search(query)
        results = list(results)
        results = list(results[0])
        console.print(
            f"[cyan bold][^][/cyan bold] [green bold]Found [yellow3 bold]{len(results)}[/yellow3 bold] results...[/green bold]"
        )
        sleep(1)
        console.print("[green bold].[/green bold]" * 110, "\n")
        sleep(1)
        for i in results:
            for key, value in i.items():
                if isinstance(value, dict):
                    console.print(
                        Panel(
                            f"[cyan bold]{str(key)}[/cyan bold]:",
                            expand=False,
                            border_style="red",
                        )
                    )
                    console.print(Panel(str(value), expand=False, border_style="green"))
                elif isinstance(value, list):
                    console.print(
                        Panel(
                            f"[cyan bold]{str(key)}[/cyan bold]:",
                            expand=False,
                            border_style="red",
                        )
                    )
                    for item in value:
                        if isinstance(item, dict):
                            console.print(
                                Panel(str(item), expand=False, border_style="green")
                            )
                        else:
                            console.print(
                                Panel(str(item), expand=False, border_style="green")
                            )
                else:
                    console.print(
                        Panel(
                            f"[cyan bold]{str(key)}[/cyan bold]: {str(value)}",
                            expand=False,
                            border_style="red",
                        )
                    )
            console.print("[yellow3 bold]=[/yellow3 bold]" * 160 + ">\n\n")
    except (
        CensysAPIException,
        CensysException,
        CensysInvalidAPIKeyException,
        CensysRateLimitExceededException,
        CensysSearchAPIErrorException,
        CensysSearchAPITimeoutException,
        CensysSearchException,
        CensysUnauthorizedException,
    ) as e:
        print(f"Error: {e}")
        exit(1)
    except KeyboardInterrupt:
        console.print("\nExiting...\n", style="bold red blink")
        exit(1)
    except Exception as e:
        console.print("\nExiting...\n", style="bold red blink")
        exit(1)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="A Python script to search using Censys.io API."
    )
    parser.add_argument("-q", "--query", help="The query to search for", type=str)
    args = parser.parse_args()
    try:
        if not args.query:
            banner()
            query = str(input(f"{OKGREEN}{BOLD}Enter the query to search for:{ENDC} "))
            check_api_key()
            main(query)
        else:
            banner()
            query = str(args.query)
            check_api_key()
            main(query)
    except KeyboardInterrupt:
        console.print("\nExiting...\n", style="bold red blink")
        exit(1)
