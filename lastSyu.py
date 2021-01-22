import subprocess

raw = subprocess.check_output("cat /var/log/pacman.log | grep Syu | tail -1 | awk '{print $1}'", shell=True).decode('UTF-8')
print("Last updated:", raw.split('T')[0][1:], "at", raw.split('T')[1][:-7])
