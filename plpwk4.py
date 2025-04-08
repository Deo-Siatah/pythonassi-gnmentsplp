
#1.CREATING THE TWO FILES 
with open("plpfile1.txt","w")as file:
    file.write("There are 26 letters in English language")
     
    
with open("output.txt","w")as file:
    file.write("The annual migration of wildebeest, zebras, and other herbivores across the Mara River from Kenya's Maasai Mara to Tanzania's Serengeti is often referred to as the Eighth Wonder of the World!")


#ASSIGNMENT:
#file names 
input_file="plpfile1.txt"
output_file="output.txt"

#Read the content of the input file
with open(input_file,"r") as file:
    content=file.read()
    
print(f"content of input file:\n{content}")
    
#modify the output_file content(convert to uppercase)
modified_content=content.upper()
with open(output_file,"w") as file:
    file.write(modified_content)
    
print(f"modified content has been saved in {output_file}")