import datetime
import time
from faker import Faker

fake = Faker('en_CA')

date = str(datetime.date.today())
fn = fake.first_name_male() #Change 'male' to 'female' for female names
fln = fake.last_name_male() #Change 'male' to 'female' for female names
fa = fake.address()
fj = fake.job()
fc = fake.company()
fce = fake.company_email()
ffe = = fake.free_email()

with open('fiddb.txt', 'w') as f:
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write(fn + ' ')
    f.write(fln)
    f.write('\n')
    f.write(fa)
    f.write('\n')
    f.write(fj)
    f.write('\n')
    f.write(fc)
    f.write('\n')
    f.write(fce)
    f.write(ffe)
    f.write('\n')
    f.write('\n')
    f.write(date)

print('Fake id created!')
time.sleep(1)
print(fn)
print(fa)
print(fj)
print(fc)
print(fce)
print('\n')
print('Generated at ' + date)
exit()
