#!/usr/bin/env python3

import os, signal, sys
import subprocess

TIMU_DIR = "timu-example"   # 存放题目的目录
SUBP_LIST = []
PORT_START = 8010   # 默认起始端口


def print_red(str):
    print("\033[1;31;40m%s\033[0m" % str)

def start_process(cmd, workdir="."):
    SUBP_LIST.append(subprocess.Popen(cmd, cwd=workdir, shell=True))

def run(path):
    global PORT_START
    print_red("[*] starting "+os.path.join(path))
    if os.path.exists(os.path.join(path, 'docker-compose.yml')):
        start_process('docker-compose up', os.path.join(path))
    elif os.path.exists(os.path.join(path, 'Dockerfile')):
        name = path.split("/")[-1]
        subprocess.Popen("docker build -t "+name+" .", cwd=os.path.join(path), shell=True).wait()
        start_process("docker run --rm --name "+name+" -p "+str(PORT_START)+":80 "+name, os.path.join(path))
        print_red("[*] started "+ path + " in port:"+str(PORT_START))
        PORT_START += 1

def signal_handler(signal, frame):
    for p in SUBP_LIST:
        try:
            p.terminate()
            p.kill()
        except:
            pass
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TIMU_DIR = sys.argv[1]
    if len(sys.argv) > 2:
        PORT_START = int(sys.argv[2])
    for dir in os.listdir(TIMU_DIR):
        if os.path.isdir(os.path.join(TIMU_DIR, dir)):
            run(os.path.join(TIMU_DIR, dir))

    for p in SUBP_LIST:
        p.wait()
