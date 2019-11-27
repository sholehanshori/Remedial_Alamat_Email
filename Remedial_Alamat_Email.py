#  ------------------------ Rabu, 27 November 2019 -----------------------------------
'''
Nama  : Sholeh Anshori Syas
Kelas : JCDS07 - Remedial
'''

# Memiliki format: namaUser@namaHosting.ekstensi
# namaUser hanya boleh terdiri atas huruf, angka, dash ('-') dan underscore ('_').
# namaHosting hanya boleh terdiri atas huruf dan angka.
# ekstensi hanya boleh terdiri atas huruf, dengan maksimum 5 karakter.

symbol = ['-', '_']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

content1 = symbol + number + letter
content2 = letter + number

def userName(isi):
    isi  = isi.lower()
    user = isi.split('@')
    for i in user[0]:
        output = False
        if i in content1:
            output = True
        else:
            output = False
            return output
    return output

def hosting(isi):
    isi   = isi.lower()
    user1 = isi.split('@')
    user2 = ''.join(user1[1])
    user3 = user2.split('.')
    for j in user3[0]:
        output = False
        if j in content2:
            output = True
        else:
            output = False
            return output
    return output

def ekstensi(isi):
    isi  = isi.lower()
    user = isi.split('.')
    count = 0
    for k in user[1]:
        output = False
        count += 1
        if count != 6:
            if k in letter:
                output = True
            else:
                output = False
        else:
            output = False
            return output
    return output

In  = input('Input email : ')
boolean = []
boolean.append(userName(In))
boolean.append(hosting(In))
boolean.append(ekstensi(In))

tick = 0
for l in boolean:
    if l == True:
        tick += 1
    else:
        tick = 0

if tick == 3:
    print('EMAIL VALID')
else:
    print('EMAIL TIDAK VALID')

print(boolean)