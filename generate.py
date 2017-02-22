from subprocess import call

N = 2000

# if we generate 2000 4MB files we have 8G of data

urls_file = open("URLs.txt", 'w')

for i in range(1, N + 1):
    # generate file with name file$i and size 4MB
    filename = "file" + str(i)
    filepath = "/home/eecs/joao/repos/files/" + filename
    print("Generating file:", filepath)

#    call(["dd", "if=/dev/urandom", "of=%s" % filepath, "bs=1024", "count=4096"])

    url = "http://localhost:800/" + filename
    urls_file.write(url + "\n")
