prev_line = None
def machine():
    machine = prev_line.split()[0]
    return machine
                
def connect():
    connect = prev_line.split()[2]
    return connect

def user():
    user = prev_line.split()
    print(user)
    return user 

with open(r'C:\Users\Jacob\Documents\sys_admin\log.smbd', 'r') as input_file, open(r'C:\Users\Jacob\Documents\sys_admin\data.txt', 'w') as output_file:
    for line in input_file:
        if "netlogon" in line: 
            pass
        if "make_connection" in line:
            parts = line.split()
            x = [parts[0], parts[1], machine(), connect(),"temp",'\n\n']
            print(parts)
            if x[3] == 'connect' or x[3] == 'closed':
                datestamp = str(x[0].replace('[',''))
                timestamp = str(x[1].replace(',',''))
                usr = str(x[2])
                con = str(x[3])
                end = str(x[4])
                output = ('"'+datestamp+'","'+timestamp+'","'+usr+'","'+con+'","'+end+'"'+"\n")
                output_file.write(output)
        prev_line = line
        
output_file.close()
