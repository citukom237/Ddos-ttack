import itertools
import threading
import time
import sys
import os


#Selamat anda tolol
#percaya apa lu ama termos sattt bangsat
#created by mr.dh0r_45


banner = """
\033[01;32m==================================================
\033[33;33mCreated   : MR.DH0R1_45
Website   : https://termux.id
Instagram : https://www.instagram.com/mrd45_gans
\033[01;32m==================================================
"""

os.system('echo -e "\033[33;33m" ')

done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r LOOANJING... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(10)
done = True

os.system('echo -e "\033[01;32m" ')
os.system('clear')
os.system("figlet 45ddos")
print (banner)

no = input("\033[33;33m - masukan no yang ingin di serang : ")
jum = int(input("\033[33;33m - masukan jumlah serangan : "))

for i in range(int(jum)):
    time.sleep(1)
    print"\033[31;31m-------[ virus TROJAN telah di kirimkan ke ",no,"]-------"

os.system('echo -e "\033[33;33m" ')
