
def parsing_txt():
    fail = open('nginx_logs.txt', encoding='UTF-8')

    array_information = []
    for line in fail.readlines():
        remote_addr = line.split()[0]
        request_type = line.split()[5].replace('"', "")
        requested_resource = line.split()[6]

        result = (remote_addr, request_type, requested_resource)
        array_information.append(result)
    return array_information

if __name__ == "__main__":
    print(parsing_txt())