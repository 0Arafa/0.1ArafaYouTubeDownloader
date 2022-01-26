import pafy
from os import rename,path,system
from time import sleep
from termcolor import cprint,colored

def banner():
    system("cls"),print("\n","\t"*3,end=""),cprint("===>  ","white",attrs=["bold"],end=""),cprint("Windows YouTube Downloader","magenta",attrs=["bold","underline"],end=""),cprint("   <===","white",attrs=["bold"],end=""),print("\t"*4,end=""),cprint("        ####  ","white",attrs=["bold"],end=""),cprint("By : Abd Almoen Arafa (0.1Arafa)","yellow",end=""),cprint("  ####","white",attrs=["bold"]),print("\t"*11,end=""),cprint("        ####  ","white",attrs=["bold"],end=""),cprint("Age : 15                         ","yellow",end=""),cprint(" ####","white",attrs=["bold"]),print("\n","\t"*2,end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("1","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Full Video","blue",attrs=["bold"]),print("\n","\t"*2,end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("2","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Only Audio","blue",attrs=["bold"]),print("\n","\t"*7,end=""),cprint("(  ","white",attrs=["bold"],end=""),cprint("Type N or No or EXIT or QUIT ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Exit The Terminal","red",attrs=["bold"],end=""),cprint(" | ","white",attrs=["bold"],end=""),cprint("CLEAR or CLS ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Clear The Terminal","red",attrs=["bold"],end=""),cprint("  )","white",attrs=["bold"])
    ask=input(colored("\n[*] Enter your choice: ","grey",attrs=["bold"])).strip()
    if ask == "2":  audio()
    elif ask == "1":    Video()
    elif ask.lower() == "n" or ask.lower() == "no" or ask.lower() == "exit" or ask.lower() == "quit":  quit()
    else:   banner()

def audio():
    def converting():
        try:
            cprint("[+] Converting to flac....","green",attrs=["bold"])
            if path.exists(video.title+".webm"):  rename(video.title+".webm",video.title+".flac"),cprint("[+] Done..","green",attrs=["bold"])
            elif path.exists(video.title+".mp3"): rename(video.title+".mp3",video.title+".flac"),cprint("[+] Done..","green",attrs=["bold"])
            elif path.exists(video.title+".m4a"): rename(video.title+".m4a",video.title+".flac"),cprint("[+] Done..","green",attrs=["bold"])
        except: cprint("[-] Error while converting to flac","red"),audio()
        finally:    sleep(1),banner()
    url=input(colored("\n[*] Enter The URL: ","grey",attrs=["bold"])).strip()
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit":  quit()
    elif not url:   audio()
    elif url.lower() == "cls" or url.lower() == "clear":   system("cls"),audio()
    try:    video=pafy.new(url)
    except: cprint("[-] Error,check your internet connection and you have to make sure that you're typing the write URL","red"),audio()
    if path.exists(video.title+".webm") or path.exists(video.title+".mp3") or path.exists(video.title+".m4a"):
        cprint("[++] This file is already installed but it's not flac","cyan")
        ask=input(colored("[*] Do you want to convert it to flac? (Y, N): ","grey",attrs=["bold"])).strip()
        if ask.lower() == "y" or ask.lower() == "yes":  converting()
        else:   audio()
    elif path.exists(video.title+".flac"):  cprint("[++] This file is already installed","cyan"),audio()
    print("\n",video,"\n")
    bestaudio=video.getbestaudio()
    try:    connection=bestaudio.download()
    except: cprint("[-] Connection Error, trying to connect...\n","red"),connection
    converting()

def Video():
    url=input(colored("\n[*] Enter The URL: ","grey",attrs=["bold"])).strip()
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit":  quit()
    elif not url:   Video()
    elif url.lower() == "cls" or url.lower() == "clear":   system("cls"),Video()
    try:    video=pafy.new(url)
    except: cprint("[-] Error,check your internet connection and you have to make sure that you're typing the write URL","red"),Video()
    if path.exists(video.title+".webm") or path.exists(video.title+".mp4") or path.exists(video.title+".3gp"):  cprint("[++] This file is already installed","cyan"),Video()
    print("\n",video)
    streams=list(video.streams)
    count=0
    for quality in streams:
        cprint("\n[ ","grey",attrs=["bold"],end=""),cprint(f"{count}","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint(f"{quality}".replace("normal:",""),"blue",attrs=["bold"],end="")
        count+=1
    try:
        ask=int(input(colored("\n\n[*] Chose The Resolution: ","grey",attrs=["bold"])))
        stream=streams[ask]
    except IndexError:  cprint("[-] Invalid Number","red"),Video()
    except: cprint("[-] You have to write just a numbers here","red"),Video()
    cprint(f"[+] The Resolution is: {streams[ask]}\n".replace("normal:",""),"green",attrs=["bold"])
    try:    connection=stream.download()
    except: cprint("[-] Connection Error, trying to connect...\n","red"),connection
    cprint("[+] Done..","green",attrs=["bold"]),sleep(1),banner()

banner()
#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
