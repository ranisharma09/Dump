import os, sys, platform
try:
    import requests
except:
	
    os.system('pip install requests')
    
    os.system('xdg-open https://youtube.com/@RANITRICKER')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf R35K3.so')
except:
    pass
os.system('rm -rf R35K3.so ')
os.system('git pull')
##os.system("xdg-open https://github.com/ranisharma09")
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('R35K3.so'):
        os.system('curl -L https://github.com/suhaniroy121/-/blob/main/R35K3.cpython-311.so?raw=true -o R35K3.so') 
        import R35K3
    else:
        import R35K3
