# Memasukkan berbagai jenis barang dengan kode tertentu ke inventory yang sudah ditetapkan

# Interface:

print("==================================================================================================================================")
print("                                                     Sorting System")
print("==================================================================================================================================")
print()
print("  Klasifikasi Produk:                        Size:                                    Tujuan:")
print("- Organik                                    - Small(0-3 kg)                          - Sumatera")
print("- Kosmetik                                   - Medium(4-8 kg)                         - Jawa")
print("- Electronik                                 - Large(8-15 kg)                         - Kalimantan")
print("- Furnitur                                                                            - Sulawesi")
print("- Material                                                                            - Wilayah lain (jika opsi wilayah tidak tersedia)")
print("- Perlengkapan tulis")
print("- Lainnya (jika opsi tidak tersedia)")
print()

Inventory1 = [[0 for j1 in range(10)]for i1 in range(10)]
Inventory2 = [[0 for j2 in range(10)]for i2 in range(10)]
Inventory3 = [[0 for j3 in range(10)]for i3 in range(10)]
Inventory4 = [[0 for j4 in range(10)]for i4 in range(10)]
Inventory5 = [[0 for j5 in range(10)]for i5 in range(10)]
Inventory6 = [[0 for j6 in range(10)]for i6 in range(10)]
Inventory7 = [[0 for j7 in range(10)]for i7 in range(10)]

# Setiap matriks menandakan inventory untuk barang-barang berbeda

def add_barang(A):
   if A >= 101000000000 and A <= 102000000000:
      for i in range(10):
         for j in range(10):
            if Inventory1[i][j] == 0:
               Inventory1[i][j] = Inventory1[i][j] + A
               print("Barang dimasukkan ke Inventory 1!")
               return Inventory1[i][j]
      else:
         print("Inventory penuh!")
         return "penuh"
   elif A >= 201000000000 and A <= 202000000000:
      for i in range(10):
         for j in range(10):
            if Inventory2[i][j] == 0:
               Inventory2[i][j] = Inventory2[i][j] + A
               print("Barang dimasukkan ke Inventory 2!")
               return Inventory2[i][j]
      else:
         print("Inventory penuh!")
         return "penuh"
   elif A >= 301000000000 and A <= 302000000000:
      for i in range(10):
         for j in range(10):
            if Inventory3[i][j] == 0:
               Inventory3[i][j] = Inventory3[i][j] + A
               print("Barang dimasukkan ke Inventory 3!")
               return Inventory3[i][j]
      else:
         print("Inventory penuh!")
         return "penuh"
   elif A >= 401000000000 and A <= 402000000000:
      for i in range(10):
         for j in range(10):
            if Inventory4[i][j] == 0:
               Inventory4[i][j] = Inventory4[i][j] + A
               print("Barang dimasukkan ke Inventory 4!")
               return Inventory4[i][j]
      else:
         print("Inventory penuh!")
         return "penuh"
   elif A >= 501000000000 and A <= 502000000000:
      for i in range(10):
         for j in range(10):
            if Inventory5[i][j] == 0:
               Inventory5[i][j] = Inventory5[i][j] + A
               print("Barang dimasukkan ke Inventory 5!")
               return Inventory5[i][j]
      else:
         print("Inventory penuh!")
         return "penuh"
   elif A >= 601000000000 and A <= 602000000000:
      for i in range(10):
         for j in range(10):
            if Inventory6[i][j] == 0:
               Inventory6[i][j] = Inventory6[i][j] + A
               print("Barang dimasukkan ke Inventory 6!")
               return Inventory6[i][j]
      else:
         print("Inventory penuh!")
         return "penuh"
   elif A >= 701000000000 and A <= 702000000000:
      for i in range(10):
         for j in range(10):
            if Inventory7[i][j] == 0:
               Inventory7[i][j] = Inventory7[i][j] + A
               print("Barang dimasukkan ke Inventory 7!")
               return Inventory7[i][j]
   else:
        print("Input invalid!")

def view_inventory(I):
   if I == 1:
      for i1 in range(10):
         for j1 in range(10):
            print(str(Inventory1[i1][j1])+" ", end = ' ')
         print()
      return I
   elif I == 2:
      for i2 in range(10):
         for j2 in range(10):
            print(str(Inventory2[i2][j2])+" ", end = ' ')
         print()
      return I
   elif I == 3:
      for i3 in range(10):
         for j3 in range(10):
            print(str(Inventory3[i3][j3])+" ", end = ' ')
         print()
      return I
   elif I == 4:
      for i4 in range(10):
         for j4 in range(10):
            print(str(Inventory4[i4][j4])+" ", end = ' ')
         print()
      return I
   elif I == 5:
      for i5 in range(10):
         for j5 in range(10):
            print(str(Inventory5[i5][j5])+" ", end = ' ')
         print()
      return I
   elif I == 6:
      for i6 in range(10):
         for j6 in range(10):
            print(str(Inventory6[i6][j6])+" ", end = ' ')
         print()
      return I
   elif I == 7:
      for i7 in range(10):
         for j7 in range(10):
            print(str(Inventory7[i7][j7])+" ", end = ' ')
         print()
      return I
   else:
      print('Inventory invalid!')

def remove_barang(R):
   if R == 1:
      for i1 in range(10):
         for j1 in range(10):
            print(str(Inventory1[i1][j1])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory1[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory1[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory1[length1][length2] = Inventory1[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   elif R == 2:
      for i2 in range(10):
         for j2 in range(10):
            print(str(Inventory2[i2][j2])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory2[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory2[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory2[length1][length2] = Inventory2[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   elif R == 3:
      for i3 in range(10):
         for j3 in range(10):
            print(str(Inventory3[i3][j3])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory3[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory3[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory3[length1][length2] = Inventory3[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   elif R == 4:
      for i4 in range(10):
         for j4 in range(10):
            print(str(Inventory4[i4][j4])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory4[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory4[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory4[length1][length2] = Inventory4[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   elif R == 5:
      for i5 in range(10):
         for j5 in range(10):
            print(str(Inventory5[i5][j5])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory5[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory5[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory5[length1][length2] = Inventory5[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   elif R == 6:
      for i6 in range(10):
         for j6 in range(10):
            print(str(Inventory6[i6][j6])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory6[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory6[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory6[length1][length2] = Inventory6[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   elif R == 7:
      for i7 in range(10):
         for j7 in range(10):
            print(str(Inventory7[i7][j7])+" ", end = ' ')
         print()
      print("Input kode barang yang ingin dihapus!")
      I = int(input())
      length1 = 9
      length2 = 9
      if I == 0:
         print("Kode invalid!")
      else:
         while Inventory7[length1][length2] != I:
            length1 = length1 - 1
            if length1 == -1:
               length1 = 9
               length2 = length2 - 1
               if length2 == -1:
                  print("Kode barang tidak ada!")
                  return "gagal"
         if Inventory7[length1][length2] == I:
            print("Apakah barang tersebut ingin dihapus?")
            confirm = input()
            if confirm == "yes" or confirm == "Yes":
               Inventory7[length1][length2] = Inventory7[length1][length2] - I
               print("Barang kode", I, "berhasil dihapus!")
               return I
            elif confirm == "No" or confirm == "no":
               print("Operasi dibatalkan!")
   else:
      print('Inventory invalid!')

def ProductType(T):
    Type = {    
        "Organik" : "101",
        "Kosmetik" : "201",
        "Electronik" : "301",
        "Furnitur" : "401",
        "Material" : "501",
        "Perlengkapan tulis" : "601",
        "Lainnya" : "701"
        }
    return Type.get(T, " Error")

def ProductSize(S):
    Size = {
        "Small" : "010",
        "Medium" : "020",
        "Large" : "030",
        }
    return Size.get(S, "Error")

def ProductDestination(D):
    Destination = {
        "Sumatera" : "100",
        "Jawa" : "200",
        "Sulawesi" : "300",
        "Kalimantan" : "400",
        "Wilayah lain" : "500"
        }
    return Destination.get(D, "Error")

def loop():
   print("Ingin add, remove barang atau view inventory, atau tutup interface?")
   W = input()

   if (W == "Add") or (W == "add"):
        n = 1; i = 0; a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0

        #Code Execution
        while(i < n):
            #Product Type
            Type = str(input("Jenis Produk: "))
            if(Type == "Organik" or Type == "organik"):
                TypeID = ProductType("Organik")
            elif(Type == "Kosmetik" or Type == "kosmetik"):
                TypeID = ProductType("Kosmetik")
            elif(Type == "Electronik" or Type == "electronik"):
                TypeID = ProductType("Electronik")
            elif(Type == "Furnitur" or Type == "furnitur"):
                TypeID = ProductType("Furnitur")
            elif(Type == "Material" or Type == "material"):
                TypeID = ProductType("Material")
            elif(Type == "Perlengkapan tulis" or Type == "perlengkapan tulis"):
                TypeID = ProductType("Perlengkapan tulis")
            elif(Type == "Lainnya" or Type == "lainnya"):
                TypeID = ProductType("Lainnya")

            #Product Size
            Size = str(input("Ukuran: "))
            if(Size == "Small" or Size == "small"):
                SizeID = ProductSize("Small")
            elif(Size == "Medium" or Size == "medium"):
                SizeID = ProductSize("Medium")
            elif(Size == "Large" or Size == "large"):
                SizeID = ProductSize("Large")

            #Product Destination
            Destination = str(input("Tujuan: "))
            if(Destination == "Sumatera" or Destination == "sumatera"):
                DestinationID = ProductDestination("Sumatera")
            elif(Destination == "Jawa" or Destination == "jawa"):
                DestinationID = ProductDestination("Jawa")
            elif(Destination == "Sulawesi" or Destination == "sulawesi"):
                DestinationID = ProductDestination("Sulawesi")
            elif(Destination == "Kalimantan" or Destination == "kalimantan"):
                DestinationID = ProductDestination("Kalimantan")
            elif(Destination == "Wilayah lain" or Destination == "wilayah lain"):
                DestinationID = ProductDestination("Wilayah lain")

    #Product Count; ID Printing
            row = 0; Total = []
    
            ID = str(TypeID) + str(SizeID) + str(DestinationID)
            IDList = [ID]
            if(TypeID == "101"): 
                a = a + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % a))
                add_barang(int(Total[row-1] + str("%03d" % a)))
            elif(TypeID == "201"):
                b = b + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % b))
                add_barang(int(Total[row-1] + str("%03d" % b)))
            elif(TypeID == "301"):
                c = c + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % c))
                add_barang(int(Total[row-1] + str("%03d" % c)))
            elif(TypeID == "401"):
                d = d + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % d))
                add_barang(int(Total[row-1] + str("%03d" % d)))
            elif(TypeID == "501"):
                e = e + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % e))
                add_barang(int(Total[row-1] + str("%03d" % e)))
            elif(TypeID == "601"):
                f = f + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % f))
                add_barang(int(Total[row-1] + str("%03d" % f)))
            elif(TypeID == "701"):
                g = g + 1
                row = row + 1
                Total = IDList + Total
                print("Product ID:", Total[row-1] + str("%03d" % g))
                add_barang(int(Total[row-1] + str("%03d" % g)))
            #Closing Program
            print("Input 'Yes' untuk menambahkan barang lain atau tekan tombol bebas untuk kembali ke interface utama.")
            Option = str(input())
            if(Option == "Yes"):
                n = n + 1
            else :
                loop()
            i = i + 1

   elif (W == "view") or (W == "View"):
      print("Inventory mana yang barangnya ingin dilihat?")
      I = int(input())
      view_inventory(I)
      loop()
   elif (W == "remove") or (W == "Remove"):
      print("Inventory mana yang barangnya ingin di remove?")
      R = int(input())
      remove_barang(R)
      loop()
   elif (W == "Tutup") or (W == "tutup"):
       print("Have a nice day!")
       return "leave"
   else:
      print("Input invalid!")
      loop()

loop()