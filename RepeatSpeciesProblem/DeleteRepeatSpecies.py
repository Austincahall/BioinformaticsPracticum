import re
# input and output files
f = open("reptile_database_2022_03.txt", "r", encoding="utf-16 le", errors='ignore')
output = open("DeletedRepeatSpecies.txt", "w", encoding="utf-8")

#looping through the files
for line in f:
    

    # this portion grabs species names
    output.write(line[line.find("\t") + 1:line.find("\t", line.find("\t", line.find("\t") + 1) + 1)])
    output.write("\n")

    # splits line and gets rid of certain characters to make parsing the line easier
    lineList = line.split("\t")
    editedLine = lineList[6]
    editedLine = editedLine.strip('')
    my_list = editedLine.split('')

    # this pattern specifically used to add $ to make parsing easier
    pattern = r'\b([A-Z]+| — )\b'

    new_list = [re.sub(pattern, r'$\1', item) for item in my_list if item != '']
    index_list = []
    key_list = []
    out_list = []
    count = 0

    # this is the for loop that essentiall goews though them as a list and gets the index of each unique one and then uses those indexes to print out
    # the unique ones with the oldest years
    for entries in (new_list):
        count += 1
        if entries.split('$')[0].strip() not in key_list:
            index_list.append(count - 1)
            key_list.append(entries.split('$')[0].strip())
    for index in (index_list):
        out_list.append(my_list[index])

    for items in out_list:
        if items != '':
            output.write(items + "\n")

    output.write("\n")

    
output.close()
