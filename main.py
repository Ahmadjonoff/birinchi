from sqlite3 import connect

# with connect('kontaktlar.db') as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#             create table kontakt(
#                 ismi varchar,
#                 yoshi int,
#                 tel varchar,
#                 kurs varchar
#             )
#         """
#     )

import sys

if len(sys.argv) != 2:
    sys.exit('Buyruqda xatolik bo`ldi!')
buyruqlar = ['qoshish', 'qidirish', 'royxat']

buyruq = sys.argv[1]

if buyruq not in buyruqlar:
    sys.exit('Buyruqda xatolik bor!')
elif buyruq == 'qoshish':
    ismi = input('Ismini kiriting: ')
    yoshi = input('Yoshini kiriting: ')
    tel = input('Tel raqamini kiriting: ')
    kurs = input('Kursini kiriting: ')
    with connect('kontaktlar.db') as db:
        cursor = db.cursor()
        cursor.execute(
            """
                insert into kontakt values
                (?, ?, ?, ?)
            """,(ismi, yoshi, tel, kurs)
        )
    sys.exit('Kontakt qo`shildi!')
elif buyruq == 'royxat':
    with connect('kontaktlar.db') as db:
        cursor = db.cursor()
        cursor.execute(
            """
                select * from kontakt
            """
        )
        kontaktlar = cursor.fetchall()
        for i in kontaktlar:
            print(i)
elif buyruq == 'qidirish':
    ustun = input('Qaysi ustun bo`yicha ma`lumot qidirmoqchisiz(ismi, yoshi, tel, kurs): ')
    qidir = input('Qidirayotgan ma`lumotingizni kiriting: ')
    if ustun == 'ismi':
        with connect('kontaktlar.db') as db:
            cursor = db.cursor()
            cursor.execute(
                """
                    select * from kontakt where ismi = ?
                """, (qidir, )
            )
            natija = cursor.fetchall()
            for i in natija:
                print(i)
    elif ustun == 'yoshi':
        with connect('kontaktlar.db') as db:
            cursor = db.cursor()
            cursor.execute(
                """
                    select * from kontakt where yoshi = ?
                """, (qidir, )
            )
            natija = cursor.fetchall()
            for i in natija:
                print(i)
    elif ustun == 'tel':
        with connect('kontaktlar.db') as db:
            cursor = db.cursor()
            cursor.execute(
                """
                    select * from kontakt where tel = ?
                """, (qidir, )
            )
            natija = cursor.fetchall()
            for i in natija:
                print(i)
    elif ustun == 'kurs':
        with connect('kontaktlar.db') as db:
            cursor = db.cursor()
            cursor.execute(
                """
                    select * from kontakt where kurs = ?
                """, (qidir, )
            )
            natija = cursor.fetchall()
            for i in natija:
                print(i)