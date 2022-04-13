from pprint import pprint
from collections import Counter


def pars_log(line: str) -> tuple:
    requested_addr= line.split()[0]
    temp = line.split('"')[1]
    request_type = temp.split()[0]
    requested_resource = temp.split(' ')[1]
    return(requested_addr, request_type, requested_resource)






list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        logs_list = pars_log(line)
        list_out.append(logs_list)


pprint(list_out)
print(Counter([x[0] for x in list_out]).most_common(5))
