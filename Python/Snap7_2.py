import snap7.client as c
from snap7.util import *
from snap7.snap7types import *

#Program untuk membaca Memori Internal

def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas["MK"],0,byte,result)

if __name__=="__main__":
    plc = c.Client()
    print('Masukkan Alamat IP PLC')
    IP = input()
    plc.connect(IP,0,1)
    print('Masukan alamat memori internal')
    Addres = input()
    Memori = ReadMemory(plc,int(Addres),0,S7WLReal)
    print ('Memori Internal pada %MD' + Addres + ' adalah ' + str(Memori))
    #WriteMemory(plc,Addres,0,S7WLReal,3.141592)
    #print ReadMemory(plc,Addres,0,S7WLReal)