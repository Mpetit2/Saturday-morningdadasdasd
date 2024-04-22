vlan_normal=range(1,1005)
vlan_extendida=range(1006,4094)
numero_vlan=int(input("ingrese el numero de vlan:"))
if numero_vlan in vlan_normal:
    print("es vlan normal")
elif numero_vlan in vlan_extendida:
    print("es vlan extendida")
else:
    print("no corresponde a una vlan")