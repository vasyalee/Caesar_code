def rus_encrypt(ru_str):
    k = int(input('Enter shift\n'))
    res = ''
    for letter in ru_str:
        if letter.islower() and letter in rus_lower:
            res += rus_lower[rus_lower.find(letter) + int(k)]
        elif letter.isupper() and letter in rus_upper:
            res += rus_upper[rus_upper.find(letter) + int(k)]
        else:
            res += letter
    return res


def eng_encrypt(eng_str):
    k = int(input('Enter shift\n'))
    res = ''
    for letter in eng_str:
        if letter.islower() and letter in eng_lower:
            res += eng_lower[(eng_lower.find(letter) + k) % 26]
        elif letter.isupper() and letter in eng_upper:
            res += eng_upper[(eng_upper.find(letter) + k) % 26]
        else:
            res += letter
    return res

def rus_decrypt(ru_encrypted):
    k = input('Enter shift or type "all" to try them all\n')
    if k == 'all':
        sub_list = []
        res_for_all_shifts = []
        for k in range(0, 33):
            for letter in ru_encrypted:
                if letter.islower() and letter in rus_lower:
                    sub_list.append(rus_lower[(rus_lower.find(letter) - int(k)) % 32])
                elif letter.isupper() and letter in rus_upper:
                    sub_list.append(rus_upper[(rus_upper.find(letter) - int(k)) % 32])
                else:
                    sub_list.append(letter)
            res_for_all_shifts.append(''.join(sub_list))
            sub_list.clear()
        return '\n'.join(res_for_all_shifts)
    else:
        res = ''
        for letter in ru_encrypted:
            if letter.islower() and letter in rus_lower:
                res += rus_lower[(rus_lower.find(letter) - int(k)) % 32]
            elif letter.isupper() and letter in rus_upper:
                res += rus_upper[(rus_upper.find(letter) - int(k)) % 32]
            else:
                res += letter
        return res

def eng_decrypt(eng_encrypted):
    k = input('Enter shift or type "all" to try them all\n')
    if k == 'all':
        sub_list = []
        res_for_all_shifts = []
        for k in range(0, 25):
            for letter in eng_encrypted:
                if letter.islower() and letter in eng_lower:
                    sub_list.append(eng_lower[(eng_lower.find(letter) - int(k)) % 26])
                elif letter.isupper() and letter in eng_upper:
                    sub_list.append(eng_upper[(eng_upper.find(letter) - int(k)) % 26])
                else:
                    sub_list.append(letter)
            res_for_all_shifts.append(''.join(sub_list))
            sub_list.clear()
        return '\n'.join(res_for_all_shifts)


    else:
        res = ''
        for letter in eng_encrypted:
            if letter.islower() and letter in eng_lower:
                res += eng_lower[(eng_lower.find(letter) - int(k)) % 26]
            elif letter.isupper() and letter in eng_upper:
                res += eng_upper[(eng_upper.find(letter) - int(k)) % 26]
            else:
                res += letter
        return res


#alphabets
rus_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lower = 'abcdefghijklmnopqrstuvwxyz'

