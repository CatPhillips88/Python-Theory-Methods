# new_file = open('example.txt', 'r')
# print(new_file.read())
# print(new_file.readline())
# print(new_file.readlines())
new_file = open('example.txt', 'a')
new_file.write('The Burj Khalifa was named after the Sheikh Khalifa')

new_file = open('example.txt', 'r')

print(new_file.read())