"""
==========================================================
Project ULTRON
automation/system.py
==========================================================
"""

import os
import platform
import socket
import subprocess
import psutil
import datetime
from pathlib import Path


class SystemController:

    def __init__(self):

        self.system = platform.system()

    ##########################################################

    def system_info(self):

        return {
            "Operating System": platform.system(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Hostname": socket.gethostname()
        }

    ##########################################################

    def cpu_usage(self):

        return psutil.cpu_percent(interval=1)

    ##########################################################

    def memory_usage(self):

        mem = psutil.virtual_memory()

        return {
            "Total_GB": round(mem.total / (1024 ** 3), 2),
            "Used_GB": round(mem.used / (1024 ** 3), 2),
            "Available_GB": round(mem.available / (1024 ** 3), 2),
            "Percent": mem.percent
        }

    ##########################################################

    def disk_usage(self):

        disk = psutil.disk_usage("/")

        return {
            "Total_GB": round(disk.total / (1024 ** 3), 2),
            "Used_GB": round(disk.used / (1024 ** 3), 2),
            "Free_GB": round(disk.free / (1024 ** 3), 2),
            "Percent": disk.percent
        }

    ##########################################################

    def battery(self):

        battery = psutil.sensors_battery()

        if battery is None:

            return {
                "Available": False
            }

        return {
            "Available": True,
            "Percent": battery.percent,
            "Charging": battery.power_plugged
        }

    ##########################################################

    def uptime(self):

        boot = datetime.datetime.fromtimestamp(
            psutil.boot_time()
        )

        return str(
            datetime.datetime.now() - boot
        )

    ##########################################################

    def list_processes(self):

        processes = []

        for proc in psutil.process_iter(["pid", "name"]):

            try:

                processes.append(proc.info)

            except Exception:

                pass

        return processes

    ##########################################################

    def terminate_process(self, process_name):

        terminated = False

        for proc in psutil.process_iter(["name"]):

            try:

                if proc.info["name"].lower() == process_name.lower():

                    proc.kill()

                    terminated = True

            except Exception:

                pass

        return terminated

    ##########################################################

    def open_folder(self, folder):

        folder = Path(folder)

        if not folder.exists():

            return False

        if self.system == "Windows":

            os.startfile(folder)

        elif self.system == "Darwin":

            subprocess.Popen(["open", folder])

        else:

            subprocess.Popen(["xdg-open", folder])

        return True

    ##########################################################

    def lock_screen(self):

        if self.system == "Windows":

            subprocess.run(
                "rundll32.exe user32.dll,LockWorkStation"
            )

        elif self.system == "Linux":

            subprocess.run(
                ["loginctl", "lock-session"]
            )

        elif self.system == "Darwin":

            subprocess.run([
                "/System/Library/CoreServices/Menu Extras/"
                "User.menu/Contents/Resources/CGSession",
                "-suspend"
            ])

    ##########################################################

    def shutdown(self):

        if self.system == "Windows":

            os.system("shutdown /s /t 0")

        elif self.system == "Linux":

            os.system("shutdown now")

        elif self.system == "Darwin":

            os.system("sudo shutdown -h now")

    ##########################################################

    def restart(self):

        if self.system == "Windows":

            os.system("shutdown /r /t 0")

        elif self.system == "Linux":

            os.system("reboot")

        elif self.system == "Darwin":

            os.system("sudo shutdown -r now")
