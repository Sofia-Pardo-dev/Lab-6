def encode_pass(password):
    pass_list = list(password)
    en_pass = list()
    for i in pass_list:
        i = int(i)
        i += 3
        en_pass.append(i)
    pass_string = ''.join(en_pass)
    return pass_string


def menu():
    print('Menu\n' +
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
            user_pass = input('Please enter a password to encode: ')
            print(encode_pass(user_pass))
            print('Your password has been encoded and stored!')
        if user_input == '2':
            print('The encoded password is' + user_pass + 'and the original password is')
        if user_input == '3':
            break

