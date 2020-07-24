print ("name module : {}".format(__name__))

'''
the whole point of this file is if you run file without importing any other file (file that you wrote) 
python run the file directly but if you import another file that you wrote python run the file through the first file that you imported

'''

def main():
    print ("name module : {}".format(__name__))

if __name__ == '__main__':
    main()

''' the above code allows us to can track and give perminsion that
another file can used this file as import or not.
it is essentially a fial safe but it can be crossed by calling main() function directly
as follow:

# import file_name
file_name.main()

'''

