options = []
for i in range(54):
    options.append([])

options1 = []
for i in range(54):
    options1.append([])
    options1[i].append([])
    options1[i].append([])
    for j in range(8):
        options1[i][0].append(0)
        options1[i][1].append(0)

loop_index = 0

for b1 in [0,1]:
    for b2 in [0,1]:
        for b3 in [0,1]:
            print(f"{b1}{b2}{b3}: ", end="")
            for i in [b1, b2, b3]:
                for j in [b1, b2, b3]:
                    for k in [b1, b2, b3]:
                        for h in [0,1]:
                            cur_val = (i&((j^k)^h))
                            options[loop_index].append(cur_val)
                            if loop_index == 12 or loop_index == 11:
                                print(f"{cur_val}", end=" ")
                                print(f"{i}{j}{k}{h}", end=" ")
                            loop_index += 1
                            loop_index %= 54
            print("")
print("\n")
for b1 in [0,1]:
    for b2 in [0,1]:
        for b3 in [0,1]:
            print(f"{b1}{b2}{b3}: ", end="")
            index = int(f"{b1}{b2}{b3}", 2)
            for i_l in range(len(options)):
               for nah in [0,1]:
                val = options[i_l][index]&(options[i_l-1][index]^nah)
                options1[i_l][nah][index] = val
                #print(val, end=" ")
                if i_l==12:
                    print(val, end=" ")
                    #print(options[i_l][index], end=" ")
                    #print(options[i_l-1][index], end=" ")
            print()
print()