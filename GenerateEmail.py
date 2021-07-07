import requests
import os
import pathlib

def GetData(**kwargs):
    url = "https://www.1secmail.com/api/v1/"

    for key, value in kwargs.items():
        if url == "https://www.1secmail.com/api/v1/":
            url += '?' + str(key) + '=' + str(value)
        else:
            url += "&" + str(key) + '=' + str(value)
    
    response = requests.request("GET", url)

    data = response.json()

    return data

def DownloadData(**kwargs):
    url = "https://www.1secmail.com/api/v1/"

    for key, value in kwargs.items():
        if url == "https://www.1secmail.com/api/v1/":
            url += '?' + str(key) + '=' + str(value)
        else:
            url += "&" + str(key) + '=' + str(value)
    
    home = pathlib.Path.home()
    dir = os.path.join(home, "Downloads")

    local_filename = url.split('=')[-1]
    local_filename = os.path.join(dir, local_filename)
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=None):
                f.write(chunk)

def ClearScreen():
    _ = os.system("cls")

if __name__ == "__main__":
    UserEmail = GetData(action="genRandomMailbox")[0]

    UserName, Domain = tuple(UserEmail.split('@'))

    MailBox = GetData(action="getMessages", login=UserName, domain=Domain)

    while True:
        ClearScreen()

        print(f"Email anda adalah : {UserEmail}\n")
        print(f"Mailbox anda berisi {len(MailBox)} pesan : \n" if len(MailBox) > 0 else "Mailbox anda kosong\n")

        if len(MailBox) > 0:
            for Mail in MailBox:
                for key, value in Mail.items():
                    print("\t", str(key), " : ", str(value).replace("\n", ""))
                print()

        command = input("Masukkan command anda (refresh/fetch/quit) : ")

        if command == "refresh":
            MailBox = GetData(action="getMessages", login=UserName, domain=Domain)

        elif command == "fetch":

            while True:
                try:
                    MailID = input("Masukkan id email yang ingin di fetch : ")
                    FetchedMail = GetData(action="readMessage", login=UserName, domain=Domain, id=MailID)

                    for key, value in FetchedMail.items():
                        if type(value) is list: # BUG : Kalau heavy traffic kadang attachments tidak terlihat semua dan file download corrupted
                            print("\t", str(key), " : ")
                            for attachment in value:
                                for anotherKey, anotherValue in attachment.items():
                                    print("\t\t", str(anotherKey), " : ", str(anotherValue).replace("\n", ""))
                        else:
                            print("\t", str(key), " : ", str(value).replace("\n", ""))

                    if len(FetchedMail["attachments"]) > 0:
                        while True:
                            anotherCommand = input("Download attachments [Y/N] ? ")
                            
                            if anotherCommand == 'Y' or anotherCommand == 'y':
                                try:
                                    NamaFile = input("Nama file yang ingin di download : ")
                                    DownloadData(action="download", login=UserName, domain=Domain, id=MailID, file=NamaFile)
                                    break
                                except:
                                    print("Nama file tidak ada!")
                                    continue

                            elif anotherCommand == 'N' or anotherCommand == 'n':
                                break

                            else:
                                continue
                    else:
                        while True:
                            anotherCommand = input("Kembali ke mailbox [Y/N] ? ")

                            if anotherCommand == 'Y' or anotherCommand == 'y':
                                break
                            elif anotherCommand == 'N' or anotherCommand == 'n':
                                break
                            else:
                                continue

                        if anotherCommand == 'Y' or anotherCommand == 'y':
                            continue

                    break

                except:
                    print("id tidak ada!")
                    

        elif command == "quit":
            break

        else:
            continue