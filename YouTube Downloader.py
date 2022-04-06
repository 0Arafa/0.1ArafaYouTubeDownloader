from pafy import new
from os import path,system
from time import sleep
from termcolor import cprint
import platform

def the_cleaner():
    if platform.system() == "Windows":  system("cls")
    else:   system("clear")

def main():
    the_cleaner(),print("\t"*10,"    \033[01m\033[94mC\033[92mo\033[90md\033[91me\033[90md \033[95mB\033[96my\033[97m:\033[00m",end=""),print("\n","\t"*4,end="                  "),print("\t"*4,end=""),cprint("              By : Abd Almoen Arafa (0.1Arafa)","yellow"),print("\t"*10,end=""),cprint("              Age: 15","yellow"),print("\t"*1,end="       "),cprint("YouTube Downloader","magenta",attrs=["bold","blink"]),print("\033[90m              _____________________"),print("           ","/                       \\"),print("           |   \033[00m",end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("1","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Video+Audio","blue",attrs=["bold"],end="   \033[90m|\n\033[00m"),print("\033[90m            \\                       /\n             +---------------------+"),print("           ","/                       \\"),print("           |   \033[00m",end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("2","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Audio","blue",attrs=["bold"],end="         \033[90m|\n"),print("            \\                       /\n             +---------------------+"),print("           ","/                       \\"),print("           |   \033[00m",end=""),cprint("[ ","grey",attrs=["bold"],end=""),cprint("3","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint("Video","blue",attrs=["bold"],end="         \033[90m|\n"),print("            \\                       /\n              _____________________\033[00m"),print("\n","\t"*5,end=""),cprint("(  ","white",attrs=["bold"],end=""),cprint("Write N or NO or EXIT or QUIT ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Exit The Terminal","red",attrs=["bold"],end=""),cprint(" | ","white",attrs=["bold"],end=""),cprint("CLEAR or CLS ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Clear The Terminal","red",attrs=["bold"],end=""),cprint(" | ","white",attrs=["bold"],end=""),cprint("MAIN ","red",attrs=["bold"],end=""),cprint("to","red",attrs=["bold","underline"],end=""),cprint(" Back To The Main Menu","red",attrs=["bold"],end=""),cprint("  )","white",attrs=["bold"])
    ask=input("\n\033[90m[*] Enter your choice: \033[34m").strip()
    print("\033[00m",end="")
    if ask == "1":  video()
    elif ask == "2":    audio()
    elif ask == "3":    videoo()
    elif ask.lower() == "n" or ask.lower() == "no" or ask.lower() == "exit" or ask.lower() == "quit":   quit()
    else:   main()

def audio():
    url=input("\n\033[90m[*] Enter The URL: \033[34m").strip()
    print("\033[00m",end="")
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit": quit()
    elif not url:   audio()
    elif url.lower() == "cls" or url.lower() == "clear":    the_cleaner(),audio()
    elif url.lower() == "main": main()
    try:    video=new(url)
    except: cprint("[-] Error, Invalid URL or check your Internet Connection.","red"),audio()
    sym={"\\":"","/":"_","?":"",":":" -","*":"","<":"",">":"","|":"_",'"':"'"}
    Title=video.title.replace("//","_")
    Sym=Title.maketrans(sym)
    if platform.system() == "Windows" and system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp3" echo f|findstr "NONE"'):   cprint("[++] This file is already installed.","cyan"),audio()
    elif platform.system() != "Windows" and system(f'test -f "/`whoami`/Desktop/{Title.translate(Sym)}.mp3"'):  cprint("[++] This file is already installed.","cyan"),audio()
    elif path.exists(Title.translate(Sym)+".webm.part") or path.exists(Title.translate(Sym)+".m4a.part"):   cprint("[++] This file is already installed, but it's not complete, The Download will continue.","cyan")
    elif path.exists(Title.translate(Sym)+".m4a") and platform.system() != "Windows":   cprint("[++] This file is already installed, but it's not complete, The Download will continue.","cyan")
    print("\033[35m",video)
    if platform.system() == "Windows":
        system(f'youtube-dl --extract-audio --audio-format mp3 --output %(title)s.%(ext)s {url}'),system(f'move "{Title.translate(Sym)}.mp3" "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp3"|findstr "NONE"'),cprint("\n[+] Moving The File to Desktop...","green",attrs=["bold"],end=" ")
        if system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp3" echo f|findstr "NONE"'):  print("\033[90m[\033[32mSUCCESSFULLY\033[90m]\033[00m")
        else:   print("\033[90m[\033[31mERROR\033[90m]\033[00m"),sleep(2)
    else:
        system(f"youtube-dl --extract-audio --audio-format mp3 --output '%(title)s.%(ext)s' {url}"),system(f'mv "{Title.translate(Sym)}.mp3" "/`whoami`/Desktop/{Title.translate(Sym)}.mp3"'),cprint("\n[+] Moving the file to Desktop...","green",attrs=["bold"],end=" ")
        if system(f'test -f "/$(whoami)/Desktop/{Title.translate(Sym)}.mp3"'):   print("\033[90m[\033[32mSUCCESSFULLY\033[90m]\033[00m")
        else:   print("\033[90m[\033[31mERROR\033[90m]\033[00m"),sleep(2)
    cprint("[+] Done.","green",attrs=["bold"]),sleep(1),main()

def video():
    url=input("\n\033[90m[*] Enter The URL: \033[34m").strip()
    print("\033[00m",end="")
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit": quit()
    elif not url:   video()
    elif url.lower() == "cls" or url.lower() == "clear":    the_cleaner(),video()
    elif url.lower() == "main": main()
    try:    Video=new(url)
    except: cprint("[-] Error, Invalid URL or check your Internet Connection.","red"),video()
    sym={"\\":"","/":"_","?":"",":":"_","*":"","<":"",">":"","|":"_",'"':"'"}
    Title=Video.title
    Sym=Title.maketrans(sym)
    if platform.system() == "Windows":
        if system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp4" echo f|findstr "NONE"') or system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.3gp" break'):    cprint("[++] This file is already installed.","cyan"),video()
    elif platform.system() != "Windows":
        if system(f'test -f "/`whoami`/Desktop/{Title.translate(Sym)}.mp4"') or system(f'test -f "/`whoami`/Desktop/{Title.translate(Sym)}.3gp"'):  cprint("[++] This file is already installed.","cyan"),video()
    if path.exists(Title.translate(Sym)+".mp4.part") or path.exists(Title.translate(Sym)+".3gp.part"):    cprint("[++] This file is already installed, but it's not complete, The Download will continue if you choose the same quality.","cyan")
    print("\033[35m",Video)
    streams=list(Video.streams)
    count=0
    for quality in streams:
        cprint("\n[ ","grey",attrs=["bold"],end=""),cprint(f"{count}","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint(f"{quality}".replace("normal:",""),"blue",attrs=["bold"],end="")
        count+=1
    try:
        ask=int(input("\n\n\033[90m[*] Chose The Resolution: \033[34m"))
        print("\033[00m",end="")
        stream=streams[ask]
    except IndexError:  cprint("[-] Error, Invalid number.","red"),video()
    except: cprint("[-] Error, You have to write just a numbers here.","red"),video()
    cprint(f"[+] The Resolution is: {streams[ask]}\n".replace("normal:",""),"green",attrs=["bold"])
    print("\033[35m",end="")
    try:    connection=stream.download()
    except: cprint("[-] Connection Error, trying to connect...\n","red"),connection
    cprint("\n[+] Moving The File to Desktop...","green",attrs=["bold"],end=" ")
    if platform.system() == "Windows":
        if not system(f'IF EXIST "{Title.translate(Sym)}.3gp" echo f|findstr "NONE"'):  system(f'move "{Title.translate(Sym)}.mp4" "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp4"|findstr "NONE"')
        else:   system(f'move "{Title.translate(Sym)}.3gp" "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.3gp"|findstr "NONE"')
        if system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp4" echo f|findstr "NONE"') or system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.3gp" echo f|findstr "NONE"'):    print("\033[90m[\033[32mSUCCESSFULLY\033[90m]\033[00m")
        else:   print("\033[90m[\033[31mERROR\033[90m]\033[00m"),sleep(2)
    else:
        if not system(f'test -f "{Title.translate(Sym)}.3gp"'): system(f'mv "{Title.translate(Sym)}.mp4" "/`whoami`/Desktop/{Title.translate(Sym)}.mp4"')
        else:   system(f'mv "{Title.translate(Sym)}.3gp" "/`whoami`/Desktop/{Title.translate(Sym)}.3gp"')
        if system(f'test -f "/$(whoami)/Desktop/{Title.translate(Sym)}.mp4"') or system(f'test -f "/$(whoami)/Desktop/{Title.translate(Sym)}.3gp"'):    print("\033[90m[\033[32mSUCCESSFULLY\033[90m]\033[00m")
        else:   print("\033[90m[\033[31mERROR\033[90m]\033[00m"),sleep(2)
    cprint("[+] Done.","green",attrs=["bold"]),sleep(1),main()

def videoo():
    url=input("\n\033[90m[*] Enter The URL: \033[34m").strip()
    print("\033[00m",end="")
    if url.lower() == "n" or url.lower() == "no" or url.lower() == "exit" or url.lower() == "quit": quit()
    elif not url:   videoo()
    elif url.lower() == "cls" or url.lower() == "clear":    the_cleaner(),videoo()
    elif url.lower() == "main": main()
    try:    Videoo=new(url)
    except: cprint("[-] Error, Invalid URL or check your Internet Connection.","red"),videoo()
    sym={"\\":"","/":"_","?":"",":":"_","*":"","<":"",">":"","|":"_",'"':"'"}
    Title=Videoo.title
    Sym=Title.maketrans(sym)
    if platform.system() == "Windows":
        if system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp4" echo f|findstr "NONE"') or system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.webm" break'):    cprint("[++] This file is already installed.","cyan"),videoo()
    elif platform.system() != "Windows":
        if system(f'test -f "/`whoami`/Desktop/{Title.translate(Sym)}.mp4"') or system(f'test -f "/`whoami`/Desktop/{Title.translate(Sym)}.webm"'):  cprint("[++] This file is already installed.","cyan"),videoo()
    if path.exists(Title.translate(Sym)+".mp4.part") or path.exists(Title.translate(Sym)+".webm.part"):    cprint("[++] This file is already installed, but it's not complete, The Download will continue if you choose the same quality.","cyan")
    print("\033[35m",Videoo)
    streams=list(Videoo.videostreams)
    count=0
    for quality in streams:
        cprint("\n[ ","grey",attrs=["bold"],end=""),cprint(f"{count}","green",end=""),cprint(" ]","grey",attrs=["bold"],end=""),cprint(" : ","yellow",attrs=["bold"],end=""),cprint(f"{quality}".replace("video:",""),"blue",attrs=["bold"],end="")
        count+=1
    try:
        ask=int(input("\n\n\033[90m[*] Chose The Resolution: \033[34m"))
        print("\033[00m",end="")
        stream=streams[ask]
    except IndexError:  cprint("[-] Error, Invalid number.","red"),videoo()
    except: cprint("[-] Error, You have to write just a numbers here.","red"),videoo()
    cprint(f"[+] The Resolution is: {streams[ask]}\n".replace("video:",""),"green",attrs=["bold"])
    print("\033[35m",end="")
    try:    connection=stream.download()
    except: cprint("[-] Connection Error, trying to connect...\n","red"),connection
    cprint("\n[+] Moving The File to Desktop...","green",attrs=["bold"],end=" ")
    if platform.system() == "Windows":
        if not system(f'IF EXIST "{Title.translate(Sym)}.webm" echo f|findstr "NONE"'): system(f'move "{Title.translate(Sym)}.mp4" "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp4"|findstr "NONE"')
        else:   system(f'move "{Title.translate(Sym)}.webm" "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.webm"|findstr "NONE"')
        if system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.mp4" echo f|findstr "NONE"') or system(f'IF EXIST "C:\\Users\\%username%\\Desktop\\{Title.translate(Sym)}.webm" echo f|findstr "NONE"'):   print("\033[90m[\033[32mSUCCESSFULLY\033[90m]\033[00m")
        else:   print("\033[90m[\033[31mERROR\033[90m]\033[00m"),sleep(2)
    else:
        if not system(f'test -f "{Title.translate(Sym)}.webm"'):    system(f'mv "{Title.translate(Sym)}.mp4" "/`whoami`/Desktop/{Title.translate(Sym)}.mp4"')
        else:   system(f'mv "{Title.translate(Sym)}.webm" "/`whoami`/Desktop/{Title.translate(Sym)}.webm"')
        if system(f'test -f "/$(whoami)/Desktop/{Title.translate(Sym)}.mp4"') or system(f'test -f "/$(whoami)/Desktop/{Title.translate(Sym)}.webm"'):   print("\033[90m[\033[32mSUCCESSFULLY\033[90m]\033[00m")
        else:   print("\033[90m[\033[31mERROR\033[90m]\033[00m"),sleep(2)
    cprint("[+] Done.","green",attrs=["bold"]),sleep(1),main()

if __name__ == "__main__":  main()

#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
