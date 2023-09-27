# -*- coding:utf-8 -*-

from os import mkdir,path,system,name,remove,urandom
from webbrowser import open_new_tab
from time import sleep
from shutil import rmtree
#from numpy import array,nditer
from colorama import Fore as f

#ŞİFRELEME PROGRAMI
if name == 'nt':
    clrscr_command = "cls"
else:clrscr_command = "clear"
def clear():
    system(clrscr_command)
def opened():
    print("""{}
  ______        _                       _____      _            _        _                            _
  |  ___|      | |                     |  ___|    | |          | |      (_)                          | |
  | |_ __ _ ___| |__   ___  __ _ _ __  | |__ _ __ | |_ ___ _ __| |_ __ _ _ _ __  _ __ ___   ___ _ __ | |_
  |  _/ _` |_  / '_ \ / _ \/ _` | '__| |  __| '_ \| __/ _ \ '__| __/ _` | | '_ \| '_ ` _ \ / _ \ '_ \| __|
  | || (_| |/ /| |_) |  __/ (_| | |    | |__| | | | ||  __/ |  | || (_| | | | | | | | | | |  __/ | | | |_
  \_| \__,_/___|_.__/ \___|\__,_|_|    \____/_| |_|\__\___|_|   \__\__,_|_|_| |_|_| |_| |_|\___|_| |_|\__|
William AFTON - Sami Lütfi YILDIZ
""".format(f.LIGHTRED_EX))
if name=="nt":
    kit_adres="C:/kits/"
elif name=="posix":
    #kit_adres="/sys/"
    kit_adres="/kits/"

system('chcp 1254')
#chcp 65001
clear()
charlist="abcçdefgğhijklmnoöpqrsştuüvwxyz"+"abcçdefgğhijklmnoöpqrsştuüvwxyz".upper()+"#+'-!@#$&_-)}{+,(=1234567890;"

run=True
menu=f"""\n
{f.GREEN}1{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Cihazıma özel şifre kitleri oluştur.
{f.GREEN}2{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Cihazıma özel şifre kitleri var mı kontrol et.
{f.GREEN}3{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Dosyamı şifrele.
{f.GREEN}4{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Dosyamı çöz.
{f.GREEN}5{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Kitlerimi sil.
{f.GREEN}6{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Konsolu temizle.
{f.GREEN}7{f.LIGHTRED_EX}-{f.YELLOW}){f.WHITE} Çıkış.

"""
while run:
    opened()
    print(menu)
    try:
        islem=int(input("{} > {}".format(f.LIGHTBLACK_EX,f.LIGHTBLUE_EX)))
    except:
        print(f.LIGHTRED_EX+"\nSayısal bir değer gir.")
        continue

    #KİT OLUŞTURMA KISMI
    if islem==1:
        if path.exists(kit_adres):
            print(f.LIGHTYELLOW_EX+"\nUyarı! Eğer kitiniz varsa ve yenisini oluşturmaya kalkarsınız eski kitleriniz silinir.Ve önceden şifrelenmiş dosyalarınızı çözemezsiniz!")
            end_qu=str(input(f.LIGHTBLACK_EX+"\nEminmisin(Y or N) >"+f.LIGHTBLUE_EX))
            if end_qu.lower()=="y" or end_qu.lower()=="yes":
                try:
                    uzunluk=2**int(input(f.LIGHTBLACK_EX+"\nKit karakter uzunluğu girin > "+f.LIGHTBLUE_EX))
                    if uzunluk>2:
                        if path.exists(kit_adres):
                            rmtree(kit_adres)
                        mkdir(kit_adres)
                        kit=urandom(uzunluk)
                        for c in charlist:
                            hash_file=open(kit_adres+str(c)+".kit","wb")
                            kit=urandom(uzunluk)
                            print(f.RED+c.upper(),f.MAGENTA+':',f.LIGHTBLACK_EX,kit)
                            hash_file.write(kit)
                            hash_file.close()
                        print(f.GREEN+"\nBaşarıyla yeni kitleriniz oluşturuldu.\n")
                        hash_kit=None
                    else:
                        print(f.LIGHTRED_EX+"\nEn düşük uzunluk 3 karakterdir!")
                        hash_kit=None
                        input()
                except:
                    hash_kit=None
                    print(f.LIGHTRED_EX+"\nBir hata oluştu. Uygulamayı yönetici olarak başlatmayı deneyin.")
                    #print(f"Unexpected {err}, {type(err)}")
            else:
                continue
        else:
            try:
                uzunluk=2**int(input(f.LIGHTBLACK_EX+"\nKit karakter uzunluğu girin > "+f.LIGHTBLUE_EX))
                if uzunluk>2:
                    if path.exists(kit_adres):
                        rmtree(kit_adres)
                    mkdir(kit_adres)
                    for c in charlist:
                        hash_file=open(kit_adres+str(c)+".kit","wb")
                        kit=urandom(uzunluk)
                        print(f.RED+c.upper(),f.MAGENTA+':',f.LIGHTBLACK_EX,kit)
                        hash_file.write(kit)
                        hash_file.close()

                    print(f.GREEN+"\nBaşarıyla yeni kitleriniz oluşturuldu.\n")
                else:
                    print(f.LIGHTRED_EX+"\nEn düşük uzunluk 3 karakterdir!")
                    input()
            except Exception as err:
                print(f.LIGHTRED_EX+"\nBir hata oluştu. Uygulamayı yönetici olarak başlatmayı deneyin.")
                print(f"Unexpected {err}, {type(err)}")
                
    #KONTROL KISMI
    elif islem==2:
        print(f.LIGHTYELLOW_EX+"\nKontrol başlatılıyor..\n\n")
        html_file=open("control.html","a")
        html_file.write("<br><h1>Kit control</h1><ul>")
        try:
            if path.exists(kit_adres):
                for c in charlist:
                    str(c)
                    if path.exists(kit_adres+c+".kit"):
                        wtext="<li><strong>"+c+"</strong> için kit <strong style=\"color:green;\">true</strong>.&nbsp;&nbsp;Uzunluk : <b>"+str(path.getsize(kit_adres+c+".kit"))+"</b>.</li>"
                        html_file.write(wtext)
                    else:
                        html_file.write("<li>"+c+" için kit <strong style=\"color:red;\">false</strong>.</li>")
                html_file.write("</ul>")
                html_file.close()
                open_new_tab("control.html")
                sleep(1.3)
                remove("control.html")
                print(f.GREEN+"\nKontrolünüz başarıyla tamamlandı.\n")
            else:
                html_file.write("<li><strong>Kits</strong> klasörü <strong style=\"color:red;\">false</strong>.</li>")
                html_file.write("</ul><br>")
                html_file.close()
                open_new_tab("control.html")
                sleep(1.2)
                remove("control.html")
                print(f.GREEN+"\nKontrolünüz başarıyla tamamlandı.\n")
        except:
            print(f.LIGHTRED_EX+"\nBir hata oluştu. Uygulamayı yönetici olarak başlatmayı deneyin.")
            #print(f"Unexpected {err}, {type(err)}")
    
    #ŞİFRELEME KISMI
    elif islem==3:
        fn=str(input(f.LIGHTBLACK_EX+"\nŞifrelenecek dosya : "+f.LIGHTBLUE_EX))
        try:
            if path.exists(fn):
                sifrelenmis=b""
                rf=open(fn,"r").read()
                if len(rf)>=150600:
                    print(f.LIGHTRED_EX+"\nDosya boyutu çok büyük. Bazı sorunlar çıkabilir veya dosyanız çok geç şifrelenebilir.")
                    end_qu=str(input(f.LIGHTBLACK_EX+"\nEminmisin(Y or N) >"+f.LIGHTBLUE_EX))
                    if end_qu.lower()=="y" or end_qu.lower()=="yes":
                        str(rf)
                        check_rf=rf
                        hf=open(path.splitext(fn)[0]+".fef","wb")
                        #rf=array(rf)
                        for c in rf:
                            if path.exists(kit_adres+c+".kit"):
                                sf=open(kit_adres+c+".kit","rb").read()
                                sifrelenmis+=sf
                            else:
                                sifrelenmis+=bytes(c,encoding="utf-8")
                        """BU YÖNTEM BÜYÜK SORUNLAR OLUŞTURDUĞUNDAN KALDIRILDI.HIZLI AMA GÜVENSİZ

                        sifrelenmis=rf

                        for c in charlist:
                            str(c)
                            if path.exists(kit_adres+c+".kit"):
                                sf=open(kit_adres+c+".kit","r").read()
                            else:
                                continue
                            sifrelenmis=sifrelenmis.replace(c,sf)
                        """
                        if check_rf == rf:
                            print(f.LIGHTRED_EX+"\nŞifreleme sonucu bir şey değişmedi. Eski kitleriniz silinmiş olabilir!")
                            input()
                        hf.write(sifrelenmis)
                        rf=sifrelenmis=sf=check_rf=None
                        hf.close()
                        print(f.GREEN+"\nŞifreleme başarıyla tamamlandı.\n")
                    else:
                        continue

                else:
                    str(rf)
                    hf=open(path.splitext(fn)[0]+".fef","wb")
                    check_rf=rf
                    rf=list(rf)
                    for c in rf:
                        if path.exists(kit_adres+c+".kit"):
                            sf=open(kit_adres+c+".kit","rb").read()
                            sifrelenmis+=sf
                        else:
                            sifrelenmis+=bytes(c,encoding="utf-8")
                    
                    if check_rf == rf:
                        print(f.LIGHTRED_EX+"\nŞifreleme sonucu bir şey değişmedi. Eski kitleriniz silinmiş olabilir!")
                        input()

                    hf.write(sifrelenmis)
                    rf=sifrelenmis=sf=check_rf=None
                    hf.close()
                    print(f.GREEN+"\nŞifreleme başarıyla tamamlandı.\n")

            else:
                print(f.LIGHTRED_EX+"\n{} adında bir dosya yok.".format(fn))
                input()
        except Exception as err:
            print(f.LIGHTRED_EX+"\nBir hata oluştu. Uygulamayı yönetici olarak başlatmayı deneyin.")
            print(f"Unexpected {err}, {type(err)}")

    #DEŞİFRELEME KISMI
    elif islem==4:
        df=str(input(f.LIGHTBLACK_EX+"\nDeşifre edilecek dosya : "+f.LIGHTBLUE_EX))
        if df.endswith(".fef")!=True:
            print(f.LIGHTRED_EX+"\nDosya uzantın .fef olmalı.")
            continue
        if path.exists(df):
            try:
                rf=open(df,"rb").read()
                for c in charlist:
                    str(c)
                    if path.exists(kit_adres+c+".kit"):
                        wf=open(kit_adres+c+".kit","rb").read()
                        break
                    else:
                        continue

                if len(rf)>=70600*len(wf):
                    wf=None
                    print(f.LIGHTRED_EX+"\nDosya boyutu çok büyük. Bazı sorunlar çıkabilir veya dosyanız çok geç deşifrelenebilir.")
                    end_qu=str(input(f.LIGHTBLACK_EX+"\nEminmisin(Y or N) >"+f.LIGHTBLUE_EX))
                    if end_qu.lower()=="y" or end_qu.lower()=="yes":

                        uzanti=str(input(f.LIGHTBLACK_EX+"Yeni dosyanın uzantısı : "+f.LIGHTBLUE_EX))
                        ef=open(path.splitext(df)[0]+uzanti,"w")# cozulmus dosya
                        check_rf=rf

                        for c in charlist:
                            if path.exists(kit_adres+c+".kit"):
                                sf=open(kit_adres+c+".kit","rb").read()
                                rf=rf.replace(sf,c)
                            else:
                                print(f.LIGHTRED_EX+"\nKit hatası.")
                                break

                        if check_rf == rf:
                            print(f.LIGHTRED_EX+"\nDeşifreleme sonucu bir şey değişmedi. Eski kitleriniz silinmiş olabilir!")
                            input()
                            ef.close()
                            remove(path.splitext(df)[0]+uzanti)
                            check_rf=rf=None
                        else:
                            pass

                        ef.write(rf)
                        #print(rf)
                        ef.close()
                        check_rf=rf=None
                        print(f.GREEN+"\nDeşifreleme başarıyla tamamlandı.\n")

                else:
                    uzanti=str(input(f.LIGHTBLACK_EX+"Yeni dosyanın uzantısı : "+f.LIGHTBLUE_EX))
                    ef=open(path.splitext(df)[0]+uzanti,"wb")# cozulmus dosya
                    check_rf=rf

                    for c in charlist:
                        if path.exists(kit_adres+c+".kit"):
                            sf=open(kit_adres+c+".kit","rb").read()
                            rf=rf.replace(sf,bytes(c,encoding="utf-8"))
                        else:
                            print(f.LIGHTRED_EX+"\nKit hatası.")
                            break

                    if check_rf == rf:
                        print(f.LIGHTRED_EX+"\nDeşifreleme sonucu bir şey değişmedi. Eski kitleriniz silinmiş olabilir!")
                        input()
                        ef.close()
                        remove(path.splitext(df)[0]+uzanti)
                        check_rf=rf=None
                        continue
                    else:
                        pass

                    ef.write(rf)
                    #print(rf)
                    ef.close()
                    check_rf=rf=None
                    print(f.GREEN+"\nDeşifreleme başarıyla tamamlandı.\n")

            except Exception as err:
                print(f.LIGHTRED_EX+"\nBir hata oluştu. Uygulamayı yönetici olarak başlatmayı deneyin.")
                print(f"Unexpected {err}, {type(err)}")
        else:
            print(f.LIGHTRED_EX+"\n{} adında bir dosya yok.".format(df))

    #KİT SİLME KISMI
    elif islem==5:
        if path.exists(kit_adres)==False:
            print(f.LIGHTRED_EX+"\nZaten kitin yok.")
            continue

        print(f.LIGHTYELLOW_EX+"\nUyarı! Eğer kitlerinizi silerseniz önceden şifrelenmiş dosyalarınızı çözemezsiniz!")
        end_qu=str(input(f.LIGHTBLACK_EX+"\nEminmisin(Y or N) >"+f.LIGHTBLUE_EX))
        if end_qu.lower()=="y" or end_qu.lower()=="yes":
            if path.exists(kit_adres):
                try:
                    rmtree(kit_adres)
                    print(f.GREEN+"\nKitlerin başarıyla silindi.\n")
                except Exception as err:
                    print(f.LIGHTRED_EX+"\nBir hata oluştu. Uygulamayı yönetici olarak başlatmayı deneyin.")
                    print(f"Unexpected {err}, {type(err)}")
        else:
            pass
    #KONSOL TEMİZLEME
    elif islem==6:
        clear()
    #Çıkıs
    elif islem==7:
        run=False
        del menu,charlist,kit_adres,islem,clrscr_command
        print(f.RESET)
    elif islem==1983 or islem==1987:
        e=f.RED+"""
    066 117 114 100 097 110 032 107 
    097 195 167 033 033 033 066 117
    110 117 032 110 101 114 100 101
    110 032 098 105 108 105 121 111
    114 115 117 110 033 066 117 032
    098 101 110 105 109 032 121 097
    197 159 097 109 196 177 109 032
    118 101 032 115"""+f.YELLOW+""" 105 122 032 098
    117 110 117 032 098 105 108 109
    101 109 101 108 105 115 105 110
    105 122 033 072 101 114 032 197
    159 101 121 032 098 105 114 032
    111 121 117 110 100 097 110 032
    105 098 097 114 101 116 032 100
    101 196 159 105 108 033 066 085
    046 046 046"""
        print(e,"\a\a\a")
    
    else:
        print(f.LIGHTRED_EX+"\nBilinmeyen komut.")
        continue
del run
print(f.RESET)
