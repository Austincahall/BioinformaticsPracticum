import re
# here are the files, input and then output file
f = open("GeckgoBookDataCollectionV5txt.txt", "r", encoding="utf-8", errors='ignore')
output = open("HolotypingOfSpecies.txt", "w", encoding="utf-8")

# here are the regex's used to collect all the possible types if there are ones not accounted for it should be possible to just add it and copy a regex from below
#just edit the first part
Holotypes = r'Holotype:\s*([A-Z]+)\s*([^[$]+)\s*(\[[^\]]*\])?'
Syntypes = r'Syntype:\s*([A-Z]+)\s*([^[$]+)\s*(\[[^\]]*\])?'
Syntypes2 = r'Syntypes:\s*([A-Z]+)\s*([^[$]+)\s*(\[[^\]]*\])?'
Paratypes = r'Paratype:\s*([A-Z]+)\s*([^$,]+)\s*(\[[^\]]*\])?'
Paratypes2 = r'Paratypes:\s*([A-Z]+)\s*([^$[]+)\s*(\[[^\]]*\])?'
Paratypes3 = r'paratype:\s*([A-Z]+)\s*([^[]+)\s*(\[[^\]]*\])?'

Lectotype = r'Lectotype:\s*([A-Z]+)\s*([^\$[]+)\s*(\[[^\]]*\])?'
Lectotype2 = r'Lectotypes:\s*([A-Z]+)\s*([^\$[]+)\s*(\[[^\]]*\])?'

Neotypes = r'Neotype:\s*([A-Z]+)\s*([^\$[]+)\s*(\[[^\]]*\])?'

# Iconotypes = r'Iconotype:\s*([A-Z]+)\s*([^\[]+)\s*(\[[^\]]*\])?'
# note: iconotypes: there are 6 of them and they arent really important (Will add manually)

for line in f:
    # this adds our special character of the $ to make parsing easier as recommended by Dr. Uetz
    line = line.replace("paratype", "$paratype")
    line = line.replace("Paratypes:", "$Paratypes:")
    line = line.replace("Holotype", "$Holotype")
    line = line.replace("Syntypes", "$Syntypes")
    line = line.replace("", "$")

    # this line writes the species name the print statemnts do the same thing but help for looking at in in the console
    output.write(line[line.find("\t")+1:line.find("\t",line.find("\t",line.find("\t")+1)+1)] + "\n")
    # print(line[line.find("\t")+1:line.find("\t",line.find("\t",line.find("\t")+1)+1)])
    # print(line)

    # these lines write to the file each match in the list and toss out the middle match which is the data being gotten rid of
    # the print statemtns do the same thing but are for viewing information in the console
    for match in re.finditer(Holotypes, line):
        output.write(f'Holotype: {match.group(1)} {match.group(3)}' + "\n")
        # print(f'Holotype: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Syntypes, line):
        output.write(f'Syntype: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Syntype: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Syntypes2, line):
        output.write(f'Syntypes: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Syntypes: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Paratypes, line):
        output.write(f'Paratype: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Paratype: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Paratypes2, line):
        output.write(f'Paratypes: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Paratypes: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Paratypes3, line):
        output.write(f'Paratypes: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Paratypes: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Lectotype, line):
        output.write(f'Lectotype: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Lectotype: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Lectotype2, line):
        output.write(f'Lectotypes: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Lectotypes: {match.group(1)} {match.group(3)}')
    for match in re.finditer(Neotypes, line):
        output.write(f'Neotype: {match.group(1)} {match.group(3)}'+ "\n")
        # print(f'Neotype: {match.group(1)} {match.group(3)}')

    #newline helps make it look pretty in the file
    output.write("\n")
    # print()
output.close()