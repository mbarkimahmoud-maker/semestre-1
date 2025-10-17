with open("table_de_multiplication.txt","a+") as file:
    for i in range(1,11) :
        file.write(f"la table de multiplication de {i} : \n")
        for j in range(1,11):
            file.write(f" 0{i} X 0{j} = {i*j} \n")
        file.write("\n")
