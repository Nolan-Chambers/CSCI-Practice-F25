"""Uses f strings to print a multiplication table in the terminal.
"""

header = "{0:>8}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}\n{11}"
boarder = "-" * 60
print(header.format(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, boarder))

row = "{0:<0}{12:<6}{1}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}"
i = 0
while i <= 9:
    print(row.format(int(i), int(0*i), int(1*i), int(2*i), int(3*i), int(4*i), int(5*i), int(6*i), int(7*i),
                        int(8*i), int(9*i), int(10*i), ":"))
    i += 1


mult_digit_row = "{0:<0}{12:<5}{1}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}"
print(mult_digit_row.format(10, 10*0, 10*1, 10*2, 10*3, 10*4, 10*5, 10*6, 10*7, 10*8, 10*9, 10*10, ":"))
