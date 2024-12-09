def update_server_configuration(path, key, value):
    with open("server.conf", "r") as file:
        lines= file.readlines()
    with open("server.conf", "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

update_server_configuration("server.conf", "PORT","8080" )

