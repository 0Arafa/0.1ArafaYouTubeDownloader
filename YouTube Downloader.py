from pafy import new
from os import path,system
from time import sleep
from termcolor import cprint,colored
import platform

def the_cleaner():
    if platform.system() == "Windows":  system("cls")
    else:   system("clear")

def main():
    the_cleaner(),print("\n","\t"*3,end=""),cprint("===>  ","white",attrs=["bold"],end=""),cprint("YouTube Downloader","magenta",attrs=["bold","underline","blink"],end=""),cprint("   <===","white",attrs=["bold"],end=""),print("\t"*4,end=""),cprint("        ####  ","white",attrs=["bold"],end=""),cprint("By : Abd Almoen Arafa (0.1Arafa)","yellow",end=""),cprint("  ####","white",attrs=["bold"]),print("\t"*11,end=""),cprint("####  ","white",attrs=["bold"],end=""),cprint("Age : 15                         ","yellow",end=""),cprint(" ####","white",attrs=["bold"]),print("\n","\t"*2,end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("1","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Full Video","blue",attrs=["bold"]),print("\n","\t"*2,end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("2","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Only Audio","blue",attrs=["bold"]),print("\n","\t"*5,end=""),cprint("(  ","white",attrs=["bold"],end=""),cprint("Type N or No or EXIT or QUIT ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Exit The Terminal","red",attrs=["bold"],end=""),cprint(" | ","white",attrs=["bold"],end=""),cprint("CLEAR or CLS ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Clear The Terminal","red",attrs=["bold"],end=""),cprint(" | ","white",attrs=["bold"],end=""),cprint("MAIN ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Back To The Main Menu","red",attrs=["bold"],end=""),cprint("  )","white",attrs=["bold"])
    ask=input(colored("\n[*] Enter your choice: ","grey",attrs=["bold"])).strip()
    if ask == "1":  video()
    elif ask == "2":    audio()
    elif ask.lower() == "n" or ask.lower() == "no" or ask.lower() == "exit" or ask.lower() == "quit":  quit()
    else:   main()

def audio():
    url=input(colored("\n[*] Enter The URL: ","grey",attrs=["bold"])).strip()
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit":  quit()
    elif not url:   audio()
    elif url.lower() == "cls" or url.lower() == "clear":   the_cleaner(),audio()
    elif url.lower() == "main":   main()
    try:    video=new(url)
    except: cprint("[-] Error, Bad URL or check your Internet Connection","red"),audio()
    sym={"\\":"","/":"","?":"",":":"","*":"","<":"",">":"","|":"_",'"':''}
    Title=video.title
    Sym=Title.maketrans(sym)
    if path.exists(Title.translate(Sym)+".mp3"):  cprint("[++] This file is already installed","cyan"),audio()
    elif path.exists(Title.translate(Sym)+".webm.part") or path.exists(Title.translate(Sym)+".m4a.part"):  cprint("[++] This file is already installed, but it's not complete, The Download will resume","cyan")
    elif path.exists(Title.translate(Sym)+".m4a") and platform.system() != "Windows":  cprint("[++] This file is already installed, but it's not complete, The Download will resume","cyan")
    if platform.system() == "Windows":  print("\n",video,"\n"),system(f"youtube-dl --extract-audio --audio-format mp3 --output %(title)s.%(ext)s {url}"),cprint("[+] Done..","green",attrs=["bold"]),sleep(1),main()
    else:   print("\n",video,"\n"),system(f"youtube-dl --extract-audio --audio-format mp3 --output '%(title)s.%(ext)s' {url}"),cprint("[+] Done..","green",attrs=["bold"]),sleep(1),main()  

def video():
    url=input(colored("\n[*] Enter The URL: ","grey",attrs=["bold"])).strip()
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit":  quit()
    elif not url:   video()
    elif url.lower() == "cls" or url.lower() == "clear":   the_cleaner(),video()
    elif url.lower() == "main": main()
    try:    Video=new(url)
    except: cprint("[-] Error, Bad URL or check your Internet Connection","red"),video()
    sym={"\\":"","/":"","?":"",":":"","*":"","<":"",">":"","|":"_",'"':''}
    Title=Video.title
    Sym=Title.maketrans(sym)
    if path.exists(Title.translate(Sym)+".mp4") or path.exists(Title.translate(Sym)+".3gp"):  cprint("[++] This file is already installed","cyan"),video()
    elif path.exists(Title.translate(Sym)+".mp4.part") or path.exists(Title.translate(Sym)+".3gp.part"):  cprint("[++] This file is already installed, but it's not complete, The Download will resume","cyan")
    print("\n",Video)
    streams=list(Video.streams)
    count=0
    for quality in streams:
        cprint("\n[ ","grey",attrs=["bold"],end=""),cprint(f"{count}","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint(f"{quality}".replace("normal:",""),"blue",attrs=["bold"],end="")
        count+=1
    try:
        ask=int(input(colored("\n\n[*] Chose The Resolution: ","grey",attrs=["bold"])))
        stream=streams[ask]
    except IndexError:  cprint("[-] Error, Invalid Number","red"),video()
    except: cprint("[-] Error, You have to write just a numbers here","red"),video()
    cprint(f"[+] The Resolution is: {streams[ask]}\n".replace("normal:",""),"green",attrs=["bold"])
    try:    connection=stream.download()
    except: cprint("[-] Connection Error, trying to connect...\n","red"),connection
    cprint("[+] Done..","green",attrs=["bold"]),sleep(1),main()

main()

#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
