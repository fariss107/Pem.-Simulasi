#Nama : Faris Sumawijaya
#NRP : 152018076
#Kelas : C

import random
def inputdata():
    while True:
        masukan1 = input('Request(s) = ')
        masukan2 = input('Minggu ke- : ')
        if (masukan1 == '') and (masukan2 == ''):
                break
        try:
            datainput.append((int(masukan1),int(masukan2)))
        except:
            print("Input Gagal!")

def prob():
    ftot = 0
    out = []
    for z in range(len(datainput)):
        ftot += datainput[z][1]
    for z in range(len(datainput)):
        n = datainput[z][1] / ftot
        out.append(n)
    return out

def probkum(inprob):
    out = []
    out.append(inprob[0])
    panjang = len(inprob) - 1
    for z in range(panjang):
        n = out[z] + inprob[z+1]
        out.append(round(n,1))
    return out

def interval(inprobkum):
    up = []
    down = []
    down.append(0)
    for z in range((len(inprobkum))-1):
        n = inprobkum[z] + 0.001
        down.append(n)
    for z in range((len(inprobkum))):
        n = inprobkum[z]
        up.append(n)
    return down, up

def predict(banyaknya, down, up, harga):
    tot1 = 0
    tot2 = 0
    data = []
    out = []
    for z in range(banyaknya):
        data.append(random.random())
    for z in range(banyaknya):
        if (data[z] >= down[0]) and (data[z] <= up[0]):
            n=0
        elif (data[z] >= down[1]) and (data[z] <= up[1]):
            n=1
        elif (data[z] >= down[2]) and (data[z] <= up[2]):
            n=2
        out.append(n)
    data = []
    for z in  range(len(out)):
        tot1 += out[z]
        n = out[z] * harga
        tot2 += n
    print('Perkiraan Permintaan = ', tot1, 'buah')
    print('Perkiraan Pengeluaran = Rp.',tot2)

datainput = []
inputdata()
alpha = prob()
beta = probkum(alpha)
bo, ab = interval(beta)[:2]
npredict = int(input('Masukan banyak prediksi: '))
price = int(input('Masukan modal barang: '))
print('== Prediksi Montecarlo ==')
predict(npredict, bo, ab, price)
