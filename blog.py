file = open('articles.txt', 'a')
msg = input('Type the message: ')

file.write('post: {}\n'.format(msg))