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
        #  11/16/2021  Added logic to create a separate prime number file prime numbers between 100K breaks
        #
        #  11/18/2021  changed the logic to use 6k+-1 to see if the number is prime number
        #               instead of checking with previous prime numbers
        #              With change the time reduced from 1 minute for every 100 recs to
        #                 8 seconds for every 1000 recs .
        #              changed every where to generate a seprate file for every 1 million recs
        #                  instead of file for every 10000 records.
        #              still generating a consolidated file for all prime numbers.
        #
'''


import datetime

# os_path= "./data_files/"    # This is for unix env
os_path = "f:/prime_numbers/"

last_pr_num_file_name = os_path + "last_prime_num.txt"
print("Last prime number file = {}".format(last_pr_num_file_name))
l_pr_num = open(last_pr_num_file_name, mode="r")
start_pr_count = int(l_pr_num.readline().strip())
start_pr_chk_fr = int(l_pr_num.readline().strip())
l_pr_num.close()
default_start_pr_chk_fr = start_pr_chk_fr
first_prime_number = default_start_pr_chk_fr

print("Last Generated Count        = {:12,}".format(start_pr_count ))
print("Last Generated Prime Number = {:12,}".format(start_pr_chk_fr))

#  2021 1110  : Removed the input and taking it from last run
#  start_pr_chk_fr = input("What number you want to start for prime numbers  : ") or default_start_pr_chk_fr
#  start_pr_chk_fr = int(start_pr_chk_fr)

if start_pr_count > 2000000 :
   out_file_num = start_pr_count / 1000000
   out_file_num = int(out_file_num)
else:
   out_file_num = 1

current_pr_count = start_pr_count
last_pr_num_file_name = os_path + "last_prime_num.txt"
pr_num_out_file_name  = os_path + "prime_num_summ_" + '{:06d}'.format(out_file_num) +".txt"
# print ("generated file name = {} ".format(pr_num_out_file_name))
start_time  = datetime.datetime.now()

pr_num_file = os_path + "all_prime_numbers.txt"

pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")
pr_nums=open(pr_num_file, mode="r")
chk_num = start_pr_chk_fr

prime_count = 0
# prime_count = input("How Many Prime Numbers do you want : ")
# prime_count = int(prime_count)
#              Changed to accept prime_count in 100 [1-1000] (between 100 and 100,000)
while True:
    prime_count = input("How Many Thousand Prime Numbers do you want (1-100001) x 1000 : ")
    prime_count = int(prime_count)
    if prime_count > 0 and prime_count < 100001:
       break

# want_f_yn = input("Do you want to create a separate Prime Num File for Every 100K [Y/N] : ")[0].upper()
# if want_f_yn == 'Y':
#    cr_pr_file = True
#else:
#    cr_pr_file = False
cr_pr_file = True

prime_count = prime_count * 1000
# print("17. Total Prime Numbers to Generate  {} ".format(prime_count))
end_pr_count  = current_pr_count + prime_count
pr_count_down = prime_count

start_time=datetime.datetime.now()

print ("Local Start time :", start_time)

total_pr_generated = 0

pr_num_array=[]
array_item=0
st_100_time=datetime.datetime.now()

if cr_pr_file:
    if current_pr_count > 2000000:
        out_pr_file_num = current_pr_count / 1000000
        out_pr_file_num = int(out_pr_file_num)
    else:
        out_pr_file_num = 1
    pr_file_name  = os_path + "all_prime_numbers_" + '{:06d}'.format(out_pr_file_num) +".txt"
#     print ("generated Split Prime Num file name = {} ".format(pr_file_name))
    pr_file_out=open(pr_file_name, mode="a", encoding="utf-8")
    cur_pr_file_num = out_pr_file_num

# print ("Current Prime Count : {:12,}".format(current_pr_count))
# print ("End     Prime Count : {:12,}".format(end_pr_count))
# wt = input('Waiting....Press Enter to continue : ')

while current_pr_count <= end_pr_count:
        chk_num += 1
        n=chk_num
        is_prime=True

 #       print("1. Checking if number {} is prime ".format(chk_num))
 #       wt = input('Waiting....Press Enter to continue : ')


        if (n % 2 == 0) or (n % 3 == 0):
#            print ("13. Number {} is divisible by 2 or 3 By passed checking prime_num_check_loop".format(n))
            continue

        i = 5
        while i ** 2 <= n:
#           print ("Checking for {} with {}".format(n,i))
            if n % i == 0 or n % (i + 2) == 0:
#                print ("number {} is divisible by {} or {} ".format(n,i,i+2))
                is_prime = False
                i += 6
                break
            i += 6

        if is_prime:
            end_time = datetime.datetime.now()
            current_pr_count += 1
            pr_count_down -= 1
#            print("3 Prime Number Found {} is {} Time : {}".format(current_pr_count, chk_num,end_time))
#            wr_str = "Prime Number " + str(current_pr_count) + " is " + str(chk_num) + " Time : " + end_time
#            pr_num_out_file.write(wr_str + "\n")
#            wt = input('4 Prime Number Found Waiting....Press Enter to continue : ')

#            pr_nums.close()
#            pr_nums=open(pr_num_file, mode="a")
#            pr_nums.write(str(chk_num) + "\n")
#            pr_nums.close()
#            pr_nums=open(pr_num_file, mode="r")

            pr_num_array.append(chk_num)
            last_prime_num=chk_num
            total_pr_generated += 1

            if int(current_pr_count / 10000) == current_pr_count / 10000:  # print time every 100 numbers
               pr_nums.close()
               pr_nums=open(pr_num_file, mode="a")
#               print("7 Inserting prime numbers in all_prime_num file")
               for ins_pr_num in pr_num_array:
#                    print ("8 Inserting prime number {:,}".format(ins_pr_num))
                    pr_nums.write(str(ins_pr_num) + "\n")
               pr_nums.close()
               pr_nums=open(pr_num_file, mode="r")

               if cr_pr_file:
#                  print("9 Inserting prime numbers in {} file".format(pr_file_name))

                   for ins_pr_num in pr_num_array:
#                       print ("10 Inserting prime number {:,}".format(ins_pr_num))
                        new_pr_file_num = current_pr_count / 1000000
                        new_pr_file_num = int(new_pr_file_num)
                        if new_pr_file_num > cur_pr_file_num:
                            pr_file_out.close()
                            cur_pr_file_num = new_pr_file_num
                            pr_file_name = os_path + "all_prime_numbers_" + '{:06d}'.format(cur_pr_file_num) + ".txt"
                            print("11 generated Prime Num file name = {} ".format(pr_file_name))
                            wt = input('New File Generated ....Press Enter to continue : ')
                            pr_file_out = open(pr_file_name, mode="a", encoding="utf-8")
                        pr_file_out.write(str(ins_pr_num) + "\n")
                   pr_file_out.close()          # This open and close will commit/save the file
                   pr_file_out = open(pr_file_name, mode="a", encoding="utf-8")
               pr_num_array=[]
               array_item = 0

#              update the last prime number details every 1000 numbers
               l_pr_num = open(last_pr_num_file_name, mode="w")
               l_pr_num.write(str(current_pr_count) + "\n")
               l_pr_num.write(str(chk_num) + "\n")
               l_pr_num.close()
               last_prime_num_written = chk_num
               total_pr_generated_written = total_pr_generated


               end_time    = datetime.datetime.now()
               en_100_time = datetime.datetime.now()
               time_for_100 = en_100_time - st_100_time
               st_100_time = datetime.datetime.now()

               wr_str = ("Prime Number {:,} is {:,} Time : {} {:,}  {} ".format(current_pr_count,chk_num,end_time,pr_count_down, time_for_100))
               print (wr_str)
               pr_num_out_file.write(wr_str + "\n")
               pr_num_out_file.close()
               pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")
#               wt = input('Written last_prime_number file ....Press Enter to continue : ')

            if int(current_pr_count / 1000000) == current_pr_count / 1000000:  # change to new file every 100000 numbers
               out_file_num_new = current_pr_count / 1000000
               out_file_num_new = int(out_file_num_new)
               if out_file_num_new > out_file_num:
                  wr_str = ("End Time : {} ".format(end_time))
                  pr_num_out_file.write(wr_str + "\n")
                  pr_num_out_file.close()

                  out_file_num = out_file_num_new
                  pr_num_out_file_name = os_path + "prime_num_summ" + '{:06d}'.format(out_file_num) + ".txt"
                  pr_num_out_file = open(pr_num_out_file_name, mode="w", encoding="utf-8")
                  wr_str = ("Start Time : {} ".format(end_time))
                  pr_num_out_file.write(wr_str + "\n")
            continue
        is_prime = True

#        print (f" 6. value of  chk_num is {chk_num} and prime number m is {m}")
#        wt = input('Waiting....Press Enter to continue : ')


end_time = datetime.datetime.now()

# l_pr_num = open(last_pr_num_file_name, mode="w")
# l_pr_num.write(str(current_pr_count) + "\n")
# l_pr_num.write(str(last_prime_num)   + "\n")
# l_pr_num.close()

seconds_elapsed = end_time - start_time


wr_str1= ('='*50)
wr_str2= ("Local Start Time   : {}".format(start_time))
wr_str3= ("Local End   Time   : {}".format(end_time))
wr_str4= ("Elapsed Time       : {}".format(seconds_elapsed))
wr_str5= ("First prime_number : {:12,}".format(first_prime_number))
wr_str6= ("Last  prime_number : {:12,}".format(last_prime_num_written))
wr_str7= ("Last  Total Gen #  : {:12,}".format(total_pr_generated_written))
wr_str8= ('='*50)
print (wr_str1)
print (wr_str2)
print (wr_str3)
print (wr_str4)
print (wr_str5)
print (wr_str6)
print (wr_str7)
print (wr_str8)

pr_num_out_file = open(pr_num_out_file_name, mode="a", encoding="utf-8")
pr_num_out_file.write(wr_str1 + "\n")
pr_num_out_file.write(wr_str2 + "\n")
pr_num_out_file.write(wr_str3 + "\n")
pr_num_out_file.write(wr_str4 + "\n")
pr_num_out_file.write(wr_str5 + "\n")
pr_num_out_file.write(wr_str6 + "\n")
pr_num_out_file.write(wr_str7 + "\n")
pr_num_out_file.write(wr_str8 + "\n")
pr_num_out_file.close()
