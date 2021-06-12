import os
import dropbox
from dropbox.files import WriteMode 

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self , file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)
        # rb --> read binary
        for root , dirs , files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root , filename)
                relative_path = os.path.relpath(local_path , file_from)
                dropbox_path = os.path.join(file_to , relative_path)

                with open(local_path , "rb") as f:
                    dbx.files_upload(f.read() , dropbox_path , mode=WriteMode("overwrite"))
                                                

def main():
    access_token = "2n_rtZTMbAoAAAAAAAAAAQKZ1-fwtDiGG-YDWKj-l_twukan9ooILZsoKXc5WXoP"
    transferData = TransferData(access_token)
    file_from = input("Enter the Folder Path to Transfer : " )
    file_to = input("Enter the Path to Upload To Dropbox : ")
    # file_from = "C:/Users/Soham Gupta/Desktop/whj files/Phyton/dropbox/dummie.txt"
    # file_to = "/python_codes/dummie.txt"
    transferData.upload_files(file_from , file_to)
    print("File Moved")

main()
        
