zh_list = ["17", "2", "172", "4", "5", "6", "7", "8", "7", "9", "31"]
zh_num = [[["172000", "1"], "1"], "9", "24567"]


def list_bl(zh_num):
    for i in zh_num:
        if type(i) == type("1"):
            return zh_num
        else:
            for j in i:
                zh_num.append(zh_num)
                zh_num.delete(zh_num[zh_num.index(j)])
                return list_bl(zh_num)


def c(zh_list, zh_num):
    l = []
    for i in zh_list:
        for j in range(len(i)):
            for z in range(len(zh_num)):
                if i[j] in zh_num[z]:
                    i = zh_num[z]
                    l.append(i)
                    break
            else:
                l.append(i)
            break
    print(l)


c(zh_list, zh_num)
