#!/usr/bin/env python3
# Built with OduduwaLang

print('--- Itan Idanwo (Conditionals & Input) ---')
oruko = input('Kini oruko re? ')
print(f'E kaabo, {oruko}!')
ojo_ori_str = input('Omo odun melo ni e? ')
print('--- Ipele Idanwo ---')
ojo_ori = 20
if (ojo_ori < 13):
    print('O jẹ ọmọdé (You are a child).')
elif (ojo_ori < 20):
    print('O jẹ ọdọ (You are a teenager).')
elif (ojo_ori < 60):
    print('O jẹ àgbàlagbà (You are an adult).')
else:
    print('O ti gbó (You are elderly).')