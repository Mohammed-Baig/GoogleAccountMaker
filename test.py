#test file to test libraries and various other services

#driver.get('http://whatismyipaddress.com')

def main():
    df = open('users.txt', 'a')
    df.write('We will be seeing an interated printing of numbers between 0 to 10\n')
    x = 0
    while(x < 11):
        df.write(str(x))
        df.write(' ')
        df.write("ooga booga")
        df.write('\n')
        x+=1
    df.close()



if __name__ == "__main__":
    main()