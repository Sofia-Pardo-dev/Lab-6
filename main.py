def encode_pass(password):
    pass_list = list(password)
    en_pass = list()
    for i in pass_list:
        i = int(i)
        i += 3
        en_pass.append(str(i))
    en_pass = ''.join(en_pass)
    return en_pass


def decode(enc_password):
    list_encpassword = list(enc_password)
    for i in range(0, len(enc_password)):
        list_encpassword[i] = str(int(enc_password[i]) - 3)
        i += 1
    return "".join(list_encpassword)


def menu():
    print('\nMenu\n' +
          '-------------\n' +
          '1. Encode\n' +
          '2. Decode\n' +
          '3. Quit\n')


if __name__ == '__main__':
    user_input = 0
    while True:
        menu()
        user_input = input('Please enter an option: ')
        if user_input == '1':
            user_pass = input('Please enter your password to encode: ')
            encoded = encode_pass(user_pass)
            print('Your password has been encoded and stored!')
        if user_input == '2':
            print('The encoded password is, ' + encoded + ' and the original password is ' + decode(user_pass) + '.')
        if user_input == '3':
            break

