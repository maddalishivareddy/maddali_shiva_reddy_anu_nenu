import os

cred_username = "maddali"
cred_password = "reddy_rules"

def filter_v1(cmd):
    blacklist = ['&&', ';', '|', '`', '$(', 'cat', 'less', 'more', 'head', 'tail']
    return not any(b in cmd for b in blacklist)

def filter_v2(cmd):
    blacklist = ['&&', ';', '|', '`', '$(', 'cat', 'less', 'more', 'head', 'tail', ' ']
    return not any(b in cmd for b in blacklist)

def filter_v3(cmd):
    blacklist = ['&&', ';', '|', '`', '$(', 'flag', 'cat', 'less', 'more', 'head', 'tail', ' ']
    return not any(b in cmd for b in blacklist)

def filter_v4(cmd):
    blacklist = ['&&', ';', '|', '`', '$(', 'flag', 'cat', 'less', 'more', 'head', 'tail', ' ', '0','1','2','3','4','5','6','7','8','9']
    return not any(b in cmd for b in blacklist)

def filter_v5(cmd):
    allowed_prefixes = ['echo', 'grep', 'cut']
    return any(cmd.startswith(ap) for ap in allowed_prefixes) and ('|' not in cmd) and (';' not in cmd) and ('&&' not in cmd)

filters = [filter_v1, filter_v2, filter_v3, filter_v4, filter_v5]

def check_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == cred_username and password == cred_password:
        print("Login successful. You get 5 tries to extract data.")
        for i in range(5):
            print(f"\nAttempt {i+1} of 5:")
            cmd = input("Command: ")
            if filters[i](cmd):
                os.system(cmd)
            else:
                print("Command rejected. Not allowed due to security policy.")
        print("No more attempts. Access revoked.")
    else:
        print("Access Denied.")

if __name__ == "__main__":
    check_credentials()
