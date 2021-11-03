# import math
import time

me_count = 0
chk_num = 1

prime_count = input("How Many Prime Numbers do you want : ")
prime_count = int(prime_count)
x = 3
start_time=time.asctime( time.localtime(time.time()) )
print ("Local Start time :", start_time)
pr_num_file = "/prime_numbers/all_prime_numbers.txt"

pr_nums=open(pr_num_file, mode="r")

while x <= prime_count:
    chk_num += 2
    m = 1
    is_prime = True
    pr_nums.seek(0)   # return to top of file

    while True:
        m = pr_nums.readline().strip()

        if m == '':
            end_time = time.asctime(time.localtime(time.time()))
            print(f"Prime Number {x} is {chk_num} Time : {end_time}")
            is_prime = False
            pr_nums.close()
            pr_nums=open(pr_num_file, mode="a")
            pr_nums.write(str(chk_num) + "\n")
            pr_nums.close()
            pr_nums=open(pr_num_file, mode="r")
            x += 1
            break

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

