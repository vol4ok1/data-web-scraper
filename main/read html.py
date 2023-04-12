with open('simple.html', 'r' ) as f:
    f_content = f.read()            ## Read file
    print(f_content)
    f_content = f.close()