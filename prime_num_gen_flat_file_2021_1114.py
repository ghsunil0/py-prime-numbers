'''
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
Modification History

        #  11/05/2021  Checking only till the check prime number is half of the check number
        #  11/10/2021  Changed the logic for status file from prime_number to prime_number_count
        #              Supresed accepting the start number and instead taking it from last run
        #              Added logic to store the last prime_number count along with the actual last prime number
        #              The all_prime Numbers initial file
        #                  This is now updated to always open the file in append mode
        #                  to start the program the initial file with prime numbers 2, 3 should be
        #                   created manually
        #              Added count down display
        #  11/11/2021  Included os path To reduce the changes from linux to windows
        #              Changed to accept prime_count in 100 [1-1000] (between 100 and 100,000)
        #  11/12/2021  Added Displaying total numbers generated at end
        #  11/14/2021  Logic changed to write store the 100 prime numbers in the array and
        #              for every 100 prime numbers found write the array to all_prime number file
        #              TODO : This logic will only work and is tested with 1st 100 prime numbers
        #                     already generated. The logic for 1st 1000 prime numbers need to be
        #                     coded and tested.
        #              Added logic to print time taken for every 100 records along with other details
        #
'''

# import math
import time
import datetime

# os_path= "./data_files/"    # This is for unix env
os_path = "f:/prime_numbers/"

last_pr_num_file_name = os_path + "last_prime_num.txt"
print ("Last prime number file = {}".format(last_pr_num_file_name))
l_pr_num = open(last_pr_num_file_name, mode="r")
start_pr_count  = int(l_pr_num.readline().strip())
start_pr_chk_fr = int(l_pr_num.readline().strip())
l_pr_num.close()
default_start_pr_chk_fr=start_pr_chk_fr
first_prime_number=default_start_pr_chk_fr

print ("Last Generated Count        = {:12,}".format(start_pr_count ))
print ("Last Generated Prime Number = {:12,}".format(start_pr_chk_fr))

#  2021 1110  : Removed the input and taking it from last run
#  start_pr_chk_fr = input("What number you want to start for prime numbers  : ") or default_start_pr_chk_fr
#  start_pr_chk_fr = int(start_pr_chk_fr)

if start_pr_count > 200000 :
   out_file_num = start_pr_count / 100000
   out_file_num = int(out_file_num)
else:
   out_file_num = 1

current_pr_count = start_pr_count
last_pr_num_file_name = os_path + "last_prime_num.txt"
pr_num_out_file_name  = os_path + "prime_num_" + '{:06d}'.format(out_file_num) +".txt"
print ("generated file name = {} ".format(pr_num_out_file_name))
# pr_num_out_file=open(pr_num_out_file_name, mode="a", encoding="utf-8")
# start_time=time.asctime( time.localtime(time.time()) )
start_time  = datetime.datetime.now()

# pr_num_file = "./data_files/all_prime_numbers.txt"
pr_num_file = os_path + "all_prime_numbers.txt"

'''
#
#  modification 2021 1110
#  This is now updated to always open the file in append mode
#  to start the program the initial file with prime numbers 2, 3 should be
#   created manually
#
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
'''
# modification 2021 1110
#  above code is deleted and the file is now the all prime numbers is opened in read mode
#     and pr_num_out_file is always opened in append mode
#

pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")
pr_nums=open(pr_num_file, mode="r")
chk_num = start_pr_chk_fr

nrem = 0

nrem = int(nrem)

nrem = chk_num % 2

# if the start_number entered is even then take the next odd number
if nrem == 0:
   chk_num = start_pr_chk_fr + 1

prime_count = 0
# prime_count = input("How Many Prime Numbers do you want : ")
# prime_count = int(prime_count)
#              Changed to accept prime_count in 100 [1-1000] (between 100 and 100,000)
while True:
    prime_count = input("How Many Prime Numbers do you want (1-1001) x 100 : ")
    prime_count = int(prime_count)
    if prime_count > 0 and prime_count < 1001:
       break

prime_count = prime_count * 100
print  ("Total Prime Numbers to Generate  :  {:,} ".format(prime_count))
end_pr_count  = current_pr_count + prime_count -1
pr_count_down = prime_count

start_time=datetime.datetime.now()

print ("Local Start time :", start_time)

total_pr_generated = 0


pr_num_array=[]

st_100_time=datetime.datetime.now()

while current_pr_count <= end_pr_count:
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

# 11/15/2021  Checking only till the check prime number is half of the check number
#       if (m == ''):
        chk_m = int(m)
        if (m == '') or (chk_m > chk_num/2) :
# 11/15/2021  End
#            finished checking against all the previous prime numbers
            end_time = datetime.datetime.now()
#            print(f"Prime Number {x} is {chk_num} Time : {end_time}")
#            wr_str = "Prime Number " + str(x) + " is " + str(chk_num) + " Time : " + end_time
#            pr_num_out_file.write(wr_str + "\n")

            is_prime = False
#            pr_nums.close()
#            pr_nums=open(pr_num_file, mode="a")
#            pr_nums.write(str(chk_num) + "\n")
#            pr_nums.close()
#            pr_nums=open(pr_num_file, mode="r")
            pr_num_array.insert(-1,chk_num)
            last_prime_num=chk_num
            total_pr_generated += 1

            current_pr_count += 1
            pr_count_down    -= 1
            if int(current_pr_count / 100) == current_pr_count / 100:  # print time every 100 numbers
               pr_nums.close()
               pr_nums=open(pr_num_file, mode="a")
               for ins_pr_num in pr_num_array:
                    pr_nums.write(str(ins_pr_num) + "\n")
               pr_nums.close()
               pr_nums=open(pr_num_file, mode="r")
               pr_num_array=[]

               end_time    = datetime.datetime.now()
               en_100_time = datetime.datetime.now()
               time_for_100 = en_100_time - st_100_time
               st_100_time = datetime.datetime.now()

               #                print("Prime Number {:,} is {:,} Time : {} {:,}".format(current_pr_count,chk_num,end_time,pr_count_down))
#               wr_str = "Prime Number " + str(current_pr_count) + " is " + str(chk_num) + " Time : " + end_time
               wr_str = ("Prime Number {:,} is {:,} Time : {} {:,}  {} ".format(current_pr_count,chk_num,end_time,pr_count_down, time_for_100))
               print (wr_str)
               pr_num_out_file.write(wr_str + "\n")
               pr_num_out_file.close()
               pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")

            if int(current_pr_count / 100000) == current_pr_count / 100000:  # change to new file every 100000 numbers
               out_file_num_new = current_pr_count / 100000
               out_file_num_new = int(out_file_num_new)
               if out_file_num_new > out_file_num:
                  wr_str = "End Time : " + end_time
                  pr_num_out_file.write(wr_str + "\n")
                  pr_num_out_file.close()

                  out_file_num = out_file_num_new
                  pr_num_out_file_name = os_path + "prime_num_" + '{:06d}'.format(out_file_num) + ".txt"
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

end_time = datetime.datetime.now()

l_pr_num = open(last_pr_num_file_name, mode="w")
l_pr_num.write(str(current_pr_count) + "\n")
l_pr_num.write(str(last_prime_num)   + "\n")
l_pr_num.close()

seconds_elapsed = end_time - start_time
print ('='*25)
print ("Local Start Time   : {}".format(start_time))
print ("Local End   Time   : {}".format(end_time))
print ("Elapsed Time       : {}".format(seconds_elapsed))
print ("First prime_number : {:12,}".format(first_prime_number))
print ("Last  prime_number : {:12,}".format(last_prime_num))
print ("Last  Total Gen #  : {:12,}".format(total_pr_generated))
print ('='*25)
