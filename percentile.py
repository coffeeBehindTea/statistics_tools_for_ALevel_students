from math import ceil
element_number = int(input("element number= "))
print(element_number)


#! init part
# x list
x = []
# frequency to each x
frequency = []
# cumulative frequency until x
cu_frequency = []

#! input data
for i in range(element_number):
    temp_x = int(input("x= "))
    temp_frequency = int(input("frequency= "))
    x.append(temp_x)
    frequency.append(temp_frequency)
    if (i > 0):
        cu_frequency.append(frequency[i] + cu_frequency[i-1])
    else:
        cu_frequency.append(temp_frequency)

# print("x:",x,'\n',"frequency:",frequency,'\n',"cu_frequency:",cu_frequency,'\n')

#! three quatiles
fir_quatile_fre = ceil(cu_frequency[element_number-1] / 4)
fir_quatile = 0
sec_quatile_fre = ceil(cu_frequency[element_number-1] / 2)
sec_quatile = 0
thr_quatile_fre = ceil((cu_frequency[element_number-1] / 4 * 3))
thr_quatile = 0

#! calculate quatiles
fre_list = [fir_quatile,sec_quatile,thr_quatile]
fre_qua_list = [fir_quatile_fre,sec_quatile_fre,thr_quatile_fre]
# print("fre_qua_list",fre_qua_list)
for i in range(3):
    j=0
    while cu_frequency[j] < fre_qua_list[i]:
        print(cu_frequency[j],fre_qua_list[i])
        j += 1
    fre_list[i] = x[j]

print("fre_list",fre_list)

asdfdsasdfdsa = input("press Enter to continue...")