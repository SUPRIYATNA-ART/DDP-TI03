def duplikasi(list_buah):
    list_terduplikasi = []
    for buah in list_buah:
        list_terduplikasi.append(buah)
        list_terduplikasi.append(buah)

    return list_terduplikasi

buah_asli=['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terduplikasi=duplikasi(buah_asli)
print(buah_terduplikasi)