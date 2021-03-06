import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    #ExStart: GettingFoldersInformation
    client =  ImapClient("imap.gmail.com", 993, "username", "password")
    folderInfoColl = client.list_folders()

    #Iterate through the collection to get folder info one by one
    for folderInfo in folderInfoColl:
        print("Folder name is " + folderInfo.name)
    folderExtInfo = client.get_folder_info(folderInfo.name)
    print("New message count: " + str(folderExtInfo.new_message_count))
    print("Is it readonly? " + str(folderExtInfo.read_only))
    print("Total number of messages " + str(folderExtInfo.total_message_count))
    #ExEnd: GettingFoldersInformation


if __name__ == '__main__':
    run()
