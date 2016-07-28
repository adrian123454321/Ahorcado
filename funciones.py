def ahorcado(intentos):
	muneco=["______","     (",")","     _", "_","      )","("]


	if intentos==7:
		print (muneco[0])
		print (muneco[1],muneco[2])
		print (muneco[3],muneco[4])			
		print (muneco[5],muneco[6])
	
	if intentos==6:
		print (muneco[1],muneco[2])
		print (muneco[3],muneco[4])			
		print (muneco[5],muneco[6])

	if intentos==5:
		print (muneco[2])
		print (muneco[3],muneco[4])			
		print (muneco[5],muneco[6])


