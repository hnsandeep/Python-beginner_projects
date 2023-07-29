# This code is a Python script that retrieves the Wi-Fi network profiles and their passwords saved on
# a Windows computer using the `netsh` command-line tool. It uses the `subprocess` module to run the
# `netsh` commands and retrieve the output, then parses the output to extract the network profiles and
# their passwords. Finally, it prints the results in a formatted table.
import subprocess
data = (subprocess.check_output(["netsh", "wlan", "show", "profiles"]) .decode("utf-8") .split("\n") )
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for profile in profiles:
    results = (subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n"))
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))
        