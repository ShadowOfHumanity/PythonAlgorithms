#try: 
#    iLoveYouData = open("iLoveYou.txte", "r") # "r" only reads, "w" meaning write, "a" means append
#except FileNotFoundError:
#    print("File Not Found")

try:
    iLoveYouData = open("ILoveYou.txt", "w") 
    iLoveYouData.write("Hello How Are You.")
    iLoveYouData.close()
    iLoveYouData = open("ILoveYou.txt", "a")
    iLoveYouData.write("\nGood, Thank you.")
    iLoveYouData.close()
    iLoveYouData = open("ILoveYou.txt", "r")
    print(iLoveYouData.read())
except:
    print("DID NOT WRITE.")