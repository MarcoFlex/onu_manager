import os
def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def specific_onu(enter):
    if os.path.isfile(enter):
        os.remove(enter)
    file = open("lista.txt", "r")
    same_file = open("lista.txt", "r")
    for i in range(0, file_len(file.name)):
        line = file.readline()
        if line[19:31] == enter:
            new_file = open(enter, "x")
            new_file.write("config terminal\ninterface gpon ")
            new_file.write(line[0:5])
            new_file.write("\n no onu ")
            new_file.write(line[10:11])
            new_file.write("\n top\nno service-port ")
            for j in range(0, file_len(file.name)):
                new_line = same_file.readline()
                if (line[0:5] == new_line[20:25] and line[10:11] == new_line[30:31]) or (line[0:5] == new_line[21:26] and line[10:11] == new_line[31:32]):
                    service_port = new_line[13:15]
            new_file.write(service_port.strip(' '))
            new_file.write("\ncommit\n\ntop")


def all_onu():
    if os.path.isfile("all_onu.txt"):
        os.remove("all_onu.txt")
    file = open("lista.txt", "r")
    same_file = open("lista.txt", "r")
    new_file = open("all_onu.txt", "x")
    for i in range(0, file_len(file.name)):
        line = file.readline()
        if line[19:23] == "DACM":
            new_file.write("config terminal\ninterface gpon ")
            new_file.write(line[0:5])
            new_file.write("\n no onu ")
            new_file.write(line[10:11])
            new_file.write("\n top\nno service-port ")
            same_file.seek(0)
            for j in range(0, file_len(file.name)):
                new_line = same_file.readline()
                if (line[0:5] == new_line[20:25] and line[10:11] == new_line[30:31]) or (line[0:5] == new_line[21:26] and line[10:11] == new_line[31:32]):
                    service_port = new_line[13:15]
            new_file.write(service_port.strip(' '))
            new_file.write("\ncommit\n\ntop\n")


def list_onu():
    file = open("lista.txt", "r")
    print("  Itf     ONU ID   Serial Number   Oper State   Software\n--------  ------   -------------   ----------   --------------------------")
    for i in range(0, file_len(file.name)):
        line = file.readline()
        if line[19:23] == "DACM":
            print(line)


user_input = input("Digite a serial ONU especifica, ou 'todos' se desejar todos ou 'list' se quiser listar todas as ONU's: \n")
if user_input == "todos":
    all_onu()
elif user_input == "list":
    list_onu()
else:
    specific_onu(user_input)