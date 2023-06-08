import sys 
import requests 
import os

repo = "";
repo_open = open("spm.rep", "r")
if repo == None:
    print("spm repo not found.")
else:
    repo = repo_open.read();
    repo_open.close()

if sys.argv[1] == "create_repo":
    repo_file = open("spm.rep", "w") 
    repo_file.write(sys.argv[2])
    repo_file.close()
"""
if sys.argv[1] == "install_main_packages":
    response = requests.get(repo + "system-start.sh")
    open("../system-start.sh", "wb").write(response.content)
    response = requests.get(repo + "term-tash")
    open("../sud_/term-tash", "wb").write(response.content)
    open("hom/.term-tash-prompt", "w").write(" - >");
    response = requests.get(repo + "bin.sh")
    open("../bin/bin.sh", "wb").write(response.content)
    response = requests.get(repo + ".term-tash-prompt")
    open("../hom/.local_conf/.term-tash-prompt", "wb").write(response.content)
    #response = requests.get(repo + "poros-recovery-mode")
    #open("../rec/recovery_mode/poros-recovery-mode", "wb").write(response.content)
    #response = requests.get(repo + "vim-stock.tar.gz")
    #open("../sapp/cache/vim-stock.tar.gz", "wb").write(response.content)
"""

if sys.argv[1] == "-I" or sys.argv[1] == "install":
    response = requests.get(repo + sys.argv[2] + ".tar.gz")
    open("../sapp/cache/" + sys.argv[2] + ".tar.gz", "wb").write(response.content)
    os.system("tar -xzvf ../sapp/cache/" + sys.argv[2] + ".tar.gz" +" -C ../sapp/")