# import math
import time

# Last output file is 000006 and
# last output line is
#      Prime Number 638600 is 9580421 Time : Thu Oct 15 12:00:04 2020

last_pr_num_count = input("Enter Last known prime number count   : ")
last_pr_num       = input("Enter Last Known Prime Number         : ")
last_pr_num       = int(last_pr_num      )
last_pr_num_count = int(last_pr_num_count)

if last_pr_num_count > 100000 :
    out_file_num = int(last_pr_num_count / 100000)
else:
    out_file_num = 1


#  start_pr_chk_fr = input("What number you want to start for prime numbers  : ")
#  start_pr_chk_fr = int(start_pr_chk_fr)
#  if start_pr_chk_fr > 100000 :
#      out_file_num = int(start_pr_chk_fr / 100000)
#  else:
#      out_file_num = 1

pr_num_out_file_name = "/prime_numbers/prime_num_" + '{:06d}'.format(out_file_num) +".txt"
print (f"generated file name = {pr_num_out_file_name}")
# pr_num_out_file=open(pr_num_out_file_name, mode="a", encoding="utf-8")

start_time=time.asctime( time.localtime(time.time()) )

pr_num_file = "/prime_numbers/all_prime_numbers.txt"

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
    last_pr_num = 3
    x = 3
else:
    pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")
    pr_nums=open(pr_num_file, mode="r")
    x = last_pr_num_count

chk_num = last_pr_num
nrem = 0
nrem = int(nrem)
nrem = chk_num % 2

if nrem == 0:
    chk_num = chk_num + 1

prime_num_array = [4]

# Building the prime number array
for line in pr_nums:
    nnum = int(line)
    prime_num_array.insert(-1, nnum)

pr_nums.close()
pr_nums = open(pr_num_file, mode="a")

me_count = 0
prime_count = input("How Many Prime Numbers do you want : ")
prime_count = int(prime_count)

start_time=time.asctime( time.localtime(time.time()) )

print ("Local Start time :", start_time)

print(f"x = {x} prime_count = {prime_count}")
print(f"Chk num = {chk_num}")

wt = input('Waiting....Press Enter to continue : ')

#  while x <= prime_count:
while True:
    chk_num += 2
#    print(f"Checking if number {chk_num} is prime ")
#    wt = input('Waiting....Press Enter to continue : ')

    m = 1
    is_prime = True

#     while True:
    for m in prime_num_array:

#        m = pr_nums.readline().strip()
#        print(f"Checking with prime number {m} for {chk_num} ")

        if m == 4:
#            end_time = time.asctime(time.localtime(time.time()))
#            print(f"Prime Number {x} is {chk_num} Time : {end_time}")
#            wr_str = "Prime Number " + str(x) + " is " + str(chk_num) + " Time : " + end_time
#            pr_num_out_file.write(wr_str + "\n")

            is_prime = False
            pr_nums.write(str(chk_num) + "\n")
            prime_num_array.insert(-1, chk_num)
            x += 1

            if (int(x / 100) == x / 100) or (x == prime_count):
                end_time = time.asctime(time.localtime(time.time()))
                print(f"Prime Number {x:,} is {chk_num:,} Time : {end_time}")
                wr_str = "Prime Number " + str(x) + " is " + str(chk_num) + " Time : " + end_time
                pr_num_out_file.write(wr_str + "\n")

#               wr_str="Prime Number " + {:,}.format(x) + " is " + {:,}.format(chk_num) Time : {end_time}")
#               pr_num_out_file.write("Prime Number " + xstr + " is " + chk_numstr + " Time : {end_time} " + "\n")

                if x > 100000:
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

print ("Finding prime_number completed")
end_time = time.asctime( time.localtime(time.time()) )

print (f"Local Start Time : {start_time}")
print (f"Local End   Time : {end_time}")

