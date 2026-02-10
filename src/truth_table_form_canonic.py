from itertools import product
# define a logic function
def f(a,b,c,d):
	return (a and not b and not c) or (not a and not b and c and d) or (a and b and c and not d)

	
variables =['a', 'b', 'c', 'd'] # create a variable

# Create a truth table
def truth_table_display(f, variables):
	print("Truth table \n")
	print(" | ".join(variables) + "| F") # style table
	print("-" * ((4 * len(variables)) + 4))
	
	lignes = []
	for values in product([0, 1], repeat=len(variables)):
		val_dict = dict(zip(variables, values))
		result = f(**val_dict)
		lignes.append((values, result))
		print(" | ".join(str(v) for v in values) + " | " + str(int(result)))
	return lignes
		
# Write the foction logic in first and second form canonic
def form_canonic(lignes, variables):
	minterms=[]
	maxterms=[]
	for values, result in lignes:
		terms=[]
		for var, val in zip(variables, values):
			if val:
				terms.append(var)
			else:
				terms.append(f"¬{var}")
		if result :
			minterms.append(" ∧ ".join(terms))
		else:
			maxterms.append(" V ".join([f"{var}" if not val else f"¬{var}" for var, val in zip(variables, values)]))
		
	f1 = " ∧ ".join(f"({m})" for m in minterms) if minterms else " 0 "
	f2 = " V ".join(f"({m})" for m in maxterms) if maxterms else " 1 "
	return f1, f2
	
lignes = truth_table_display(f, variables)
fc1, fc2 = form_canonic(lignes, variables)

print("\n ✅️ First canonic form : ")
print("F =", fc1)
print("\n ✅️ Second canonic form : ")
print("F =", fc2)	
