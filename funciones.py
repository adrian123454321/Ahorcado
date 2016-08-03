def ahorcado (intentos):
	if intentos == 1:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +
		"| \n" +      
		"| \n" +     
		"| \n" +   
		"| \n" +     
		"|") 
	if intentos == 2:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +
		"|      ( ) \n" +      
		"| \n" +     
		"| \n" +   
		"| \n" +     
		"|") 
	if intentos == 3:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +
		"|      ( ) \n" +      
		"|       |  \n" +     
		"|       | \n" +   
		"|\n" +     
		"|") 
	if intentos == 4:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +
		"|      ( ) \n" +      
		"|       |  \n" +     
		"|       | \n" +   
		"|      / \n" +   
		"|") 
	if intentos == 5:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +
		"|      ( ) \n" +      
		"|       |  \n" +     
		"|       | \n" +   
		"|      / \  \n" +   
		"|") 
	if intentos == 6:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +   
		"|      ( ) \n" +      
		"|      _|  \n" +     
		"|       | \n" +   
		"|      / \  \n" + 
		"|") 	
	if intentos == 7:
		return ("_ _ _ _ _ \n"+
		"|       |\n" +
		"|      ( ) \n" +      
		"|      _|_  \n" +     
		"|       | \n" +   
		"|      / \  \n" + 
		"|") 

		
#		_|_
#		 |
#		/ \