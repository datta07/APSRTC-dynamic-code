#RTC project data handler project
import sqlite3
import requests

#in bst.db have table stops(stp_id,bstp_nm,bstp_cd,bus_ser)
#data from http://pubappapi.rtclivebus.com/apiv1/allbusstops?app_id=6 have dumpped into the database
#in bst.db have table bus(veh_reg_nu TEXT,veh_id NUMBER,veh_status_id NUMBER,veh_status_nm TEXT,vclass_nm TEXT)
#data from http://pubappapi.rtclivebus.com/apiv1/allVehiclesLst?app_id=6 have dumpped into the database


def find_bus(query,coloumn):
	con=sqlite3.connect('bst.db')
	l=[]
	k=con.execute('select * from bus where '+ coloumn +' = ?',(query,))
	for i in k:
		l.append(i)
	con.close()
	return l

def find_stop(query):
	con=sqlite3.connect('bst.db')
	l=[]
	k=con.execute('select * from stops where bstp_nm LIKE ?',(query+'%',))
	for i in k:
		l.append(i)
	con.close()
	return l

print(find_stop('MADANAP'))
print(find_bus('AP 28 Z 4541','veh_reg_nu'))
#print(find_stop('RAPUR'))
#input()
#print(find_stop('33'))
'''
for i in range(1,10):
	print('-'*50)
	t1=find_bus(i,'veh_id')
	print(t1)
	k=requests.get('http://pubappapi.rtclivebus.com/apiv1//trips/'+str(i)+'/trackvehicle')
	k=k.json()
	print(k['data'])
'''
#13639
k=requests.get('http://pubappapi.rtclivebus.com/apiv1//trips/'+str(13)+'/trackvehicle')
k=k.json()
print(k['data'])