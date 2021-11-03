# import math
"""
  Prime number generator :

  The program displays the last prime number generated as default start number
  accept : last prime number to start with
           how many prime numbers to generate
  process : will find the prime numbers
            store the prime numbers in a flat file
            store the last prime number in a separate parameter file
                 as the default for next run
            store the statistics for every 100 prime numbers in a
                seprate file 0-2 million in file 001
                             2-3 million in file 002
                             and so on 1 file for every million numbers
                        store the last prime number in a separate parameter file
                 as the default for next run
            at end display the start and end prime numbers and time taken
"""


import time


last_pr_num_file_name = "f:/prime_numbers/last_prime_num.txt"
l_pr_num = open(last_pr_num_file_name, mode="r")
start_pr_chk_fr = l_pr_num.readline().strip()
l_pr_num.close()
default_start_pr_chk_fr=int(start_pr_chk_fr)
first_prime_number=default_start_pr_chk_fr

print ("Last Generated Prime Number = {:,}".format(default_start_pr_chk_fr))

start_pr_chk_fr = input("What number you want to start for prime numbers  : ") or default_start_pr_chk_fr
start_pr_chk_fr = int(start_pr_chk_fr)
if start_pr_chk_fr > 100000 :
    out_file_num = start_pr_chk_fr / 100000
    out_file_num = int(out_file_num)
else:
    out_file_num = 1

last_pr_num_file_name = "f:/prime_numbers/last_prime_num.txt"
pr_num_out_file_name = "f:/prime_numbers/prime_num_" + '{:06d}'.format(out_file_num) +".txt"
print (f"generated file name = {pr_num_out_file_name}")
# pr_num_out_file=open(pr_num_out_file_name, mode="a", encoding="utf-8")

start_time=time.asctime( time.localtime(time.time()) )

pr_num_file = "f:/prime_numbers/all_prime_numbers.txt"

if out_file_num == 1:
    pr_num_out_file = open(pr_num_out_file_name, mode="w")
    wr_str = "Prime Number 2 is 2 Time : " + start_time + "\n"
    pr_num_out_file.write(wr_str)
    wr_str = "Prime Number 3 is 3 Time : " + start_time + "\n"
    pr_num_out_file.write(wr_str)
    pr_num_out_file.close()
    pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")

    pr_nums=open(pr_num_file, mode="w")
    pr_nums.write(str(2) + "\n")
    pr_nums.write(str(3) + "\n")
    pr_nums.close()
    pr_nums = open(pr_num_file, mode="r")
    start_pr_chk_fr = 3
else:
    pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")
    pr_nums=open(pr_num_file, mode="r")


chk_num = start_pr_chk_fr

nrem = 0

nrem = int(nrem)

nrem = chk_num % 2

# if the start_number entered is even then take the next odd number
if nrem == 0:
    chk_num = start_pr_chk_fr + 1

me_count = 0

prime_count = input("How Many Prime Numbers do you want : ")
prime_count = int(prime_count)

x = 4
start_time=time.asctime( time.localtime(time.time()) )

print ("Local Start time :", start_time)

while x <= prime_count:
# while True:
    chk_num += 2
#    print(f"Checking if number {chk_num} is prime ")
#    wt = input('Waiting....Press Enter to continue : ')

    m = 1
    is_prime = True
    pr_nums.seek(0)   # return to top of file

    while True:
        m = pr_nums.readline().strip()
#        print(f"Checking with prime number {m} for {chk_num} ")

        if m == '':
#            finished checking against all the previous prime numbers

#            end_time = time.asctime(time.localtime(time.time()))
#            print(f"Prime Number {x} is {chk_num} Time : {end_time}")
#            wr_str = "Prime Number " + str(x) + " is " + str(chk_num) + " Time : " + end_time
#            pr_num_out_file.write(wr_str + "\n")

            is_prime = False
            pr_nums.close()
            pr_nums=open(pr_num_file, mode="a")
            pr_nums.write(str(chk_num) + "\n")
            pr_nums.close()
            pr_nums=open(pr_num_file, mode="r")
            last_prime_num=chk_num
            x += 1

            if int(x / 100) == x / 100:  # print time every 100 numbers
                end_time = time.asctime(time.localtime(time.time()))
                print(f"Prime Number {x} is {chk_num} Time : {end_time}")
                wr_str = "Prime Number " + str(x) + " is " + str(chk_num) + " Time : " + end_time
                pr_num_out_file.write(wr_str + "\n")

                if x > 100000:  # change to new file every 100000 prime numbers
                    out_file_num_new = x / 100000
                    out_file_num_new = int(out_file_num_new)
                    if out_file_num_new > out_file_num:
                        wr_str = "End Time : " + end_time
                        pr_num_out_file.write(wr_str + "\n")
                        pr_num_out_file.close()

                        out_file_num = out_file_num_new
                        pr_num_out_file_name = "/prime_numbers/prime_num_" + '{:06d}'.format(out_file_num) + ".txt"
                        pr_num_out_file = open(pr_num_out_file_name, mode="w", encoding="utf-8")
                        wr_str = "Start Time : " + end_time
                        pr_num_out_file.write(wr_str + "\n")

            break

#        print (f" value of  chk_num is {chk_num} and prime number m is {m}")
#        wt = input('Waiting....Press Enter to continue : ')

        m = int(m)
        nrem = 0
        nrem = chk_num % m

        nrem = int(nrem)

        if nrem == 0:
            is_prime = False
            break

end_time = time.asctime( time.localtime(time.time()) )

l_pr_num = open(last_pr_num_file_name, mode="w")
l_pr_num.write(str(last_prime_num) + "\n")
l_pr_num.close()

print ("Finding prime_number completed")
print ("Local Start Time   : {start_time}")
print ("First prime_number : {:,}".format(first_prime_number))
print ("Last  prime_number : {:,}".format(last_prime_num))

print ("Last  prime_number : {last_prime_num} ")
print (f"Local End   Time  : {end_time}")

