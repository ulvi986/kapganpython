import psutil

def find_programs_and_protocols():
    connections = psutil.net_connections()
    program_connections = {}

    for conn in connections:
        pid = conn.pid
        program_name = psutil.Process(pid).name()
        protocol = conn.type

        if program_name in program_connections:
            program_connections[program_name].append((conn, protocol))
        else:
            program_connections[program_name] = [(conn, protocol)]

    return program_connections

# Örnek kullanım
connections = find_programs_and_protocols()
for program_name, connections in connections.items():
    print(f"Program: {program_name}")
    for conn, protocol in connections:
        print(f"- Bağlantı: {conn}")
        if protocol == 1:
            print("  Protokol: TCP")
        elif protocol == 2:
            print("Protokol: UDP")
    print()
