#andreas nugroho
#71200646

#andi, eka, fajar, dika, sedang bermain lempar dadu. mereka telah membuat list dari siapa yang akan di lawan yaitu 
#andi vs eka dan fajar vs dika
#peraturannya adalah pemain yang menang akan masuk ke babak final dan memperebutkan juara 1 
#pemain yang memiliki nilai dadu sama akan mendapan kesempatan lagi, dan jika 3 kali masih sama maka di anggap gugur
#buatlah aplikasi pengacak dadu untuk permainan mereka dan tentukan siapa yang menjadi pemenang 

#input 

#proses
#memakai fungsi random 
#if else 
#output
#juara 1 

#mengimport fungsi random
import random

print("-"*5,"BABAK 1","-"*5)


print("-"*19)
print("andi vs eka")
print("-"*19)

#merandom dadu 
andi = random.randint(1,6)
eka = random.randint(1,6)


print("lemparan 1 untuk andi vs eka")
#menampilkan random dadu
print ("Dadu andi =",andi,"&","Dadu eka =",eka)
print("")


if andi == eka:
    print("lemparan 2 untuk andi vs eka")
    andi1 = random.randint(1,6)
    eka1 = random.randint(1,6)
    #menampilkan hasil lemparan ke dua
    print ("Dadu andi =",andi1,"&","Dadu eka =",eka1)
    print("")

    if eka1 > andi1:
        hasil = "eka"
        print("EKA PEMENANGNYA!!!")
        input('tekan enter untuk lanjutkan')
        
    elif eka1 < andi1:
        hasil = "andi"
        print ("ANDI PEMENANGNYA!!!")
        input('tekan enter untuk lanjutkan')

    if andi1 == eka1:
        print("lemparan ke 3 untuk andi vs eka")
        #lemparan random dadu ke tiga 
        andi2 = random.randint(1,6)
        eka2 = random.randint(1,6)
        #menampilkan hasil lemparan ke tiga
        print ("Dadu andi =",andi2,"&","Dadu eka =",eka2)
        print("")
        hasil = "gugur"
        print("GUGUR DALAM PERTANDINGAN!")
        input('tekan enter untuk lanjutkan')
        
elif eka > andi:
    hasil = "eka" 
    print("EKA PEMENANGNYA")
    input('tekan enter untuk lanjutkan')

elif eka < andi:
    hasil = "andi"
    print ("ANDI PEMENANGNYA!!!")
    input('tekan enter untuk lanjutkan')

#fajar vs dika

print("-"*19)
print("fajar vs dika")
print("-"*19)

fajar = random.randint(1,6)
dika = random.randint(1,6)

print("lemparan 1 untuk fajar vs dika")
print ("Dadu fajar =",fajar,"&","Dadu dika =",dika)
print("")

if fajar == dika:
    print("lemparan 2 untuk fajar vs dika")
    fajar1 = random.randint(1,6)
    dika1 = random.randint(1,6)
    print ("Dadu fajar =",fajar1,"&","Dadu dika =",dika1)
    print("")

    if fajar1 > dika1:
        hasil1 = "fajar"
        print("FAJAR PEMENANGNYA!!!")
        input('tekan enter untuk lanjutkan')
        
    elif fajar1 < dika1:
        hasil1 = "dika"
        print ("DIKA PEMENANGNYA!!!")
        input('tekan enter untuk lanjutkan')

    if fajar1 == dika1:
        print("lemparan ke 3 untuk fajar vs dika")
        fajar2 = random.randint(1,6)
        dika2 = random.randint(1,6)
        print ("Dadu fajar =",andi2,"&","Dadu dika =",eka2)
        print("")
        hasil1 = "gugur"
        print("GUGUR DALAM PERTANDINGAN!")
        input('tekan enter untuk lanjutkan')
        
elif fajar > dika:
    hasil1 = "fajar" 
    print("FAJAR PEMENANGNYA")
    input('tekan enter untuk lanjutkan')

elif fajar < dika:
    hasil1 = "dika"
    print ("DIKA PEMENANGNYA!!!")
    input('tekan enter untuk lanjutkan')

#final

print("")
print("-"*5,"FINAL","-"*5)
print("")
print("Pemenang pertama adalah",hasil)
print("pemenang kedua adalah",hasil1)
print("")
print(hasil,"vs",hasil1)
print("")

#random dadu untuk final
lempar1 = random.randint(1,6) #hasil
lempar2 = random.randint(1,6) #hasil1

print("lemparan 1 untuk",hasil,"vs",hasil1)
#menampilkan angka lemrapan mereka
print ("Dadu",hasil,"=",lempar1,"&","Dadu",hasil1,"=",lempar2)
print("")

if lempar1 == lempar2:
    print("lemparan 2 untuk",hasil,"vs",hasil1)
    lempar3 = random.randint(1,6) #hasil
    lempar4 = random.randint(1,6) #hasil1
    print ("Dadu",hasil,"=",lempar3,"&","Dadu",hasil1,"=",lempar4)
    print("")

    if lempar3 > lempar4:
        final = hasil
        print(hasil,"1st winner!")
        input('tekan enter untuk lanjutkan')
        
    elif lempar3 < lempar4:
        final = hasil1
        print(hasil1,"1st winner!")
        input('tekan enter untuk lanjutkan')

    if lempar3 == lempar4:
        print("lemparan 3 untuk",hasil,"vs",hasil1)
        lempar5 = random.randint(1,6)
        lempar6 = random.randint(1,6)
        print ("Dadu",hasil,"=",lempar5,"&","Dadu",hasil1,"=",lempar6)
        print("")
        final = "gugur"
        print("GUGUR DALAM PERTANDINGAN!")
        input('tekan enter untuk lanjutkan')
        
elif lempar1 > lempar2:
    final = hasil 
    print(hasil,"1st winner!")
    input('tekan enter untuk lanjutkan')

elif lempar1 < lempar2:
    final = hasil1
    print(hasil1,"1st winner!")
    input('tekan enter untuk lanjutkan')
print("")
print("THE WINNER IS",final)