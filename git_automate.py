import os


while True:
    try:
        commit_message = str(input("Commit message: "))
        os.system('git add .')
        os.system('git commit -m'+commit_message)
        os.system('git push')
        break
    except KeyboardInterrupt:
        break
    except:
        print("Network not found. Retrying.")
