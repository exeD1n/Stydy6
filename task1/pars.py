def parsing_txt():
    array_info = []
    
    with open ('nginx_logs.txt', encoding='UTF-8') as f:
        for line in f:
            readline_file = line.split()

            remote_addr = readline_file[0]
            request_type = readline_file[5].replace('"', "")
            requested_resource = readline_file[6]

            result = (remote_addr, request_type, requested_resource)
            array_info.append(result)
        return array_info
        

if __name__ == "__main__":
    print(parsing_txt())