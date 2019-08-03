#4
word_1 = "разработка"
word_2 = "администрирование"
word_3 = "protocol"
word_4 = "standard"
print(word_1.encode('utf-8'))
print(word_2.encode('utf-8'))
print(word_3.encode('utf-8'))
print(word_4.encode('utf-8'))

encrtd_word_1 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
encrtd_word_2 = b'''\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'''
encrtd_word_3 = b'protocol'
encrtd_word_4 = b'standard'
print(encrtd_word_1.decode('utf-8'))
print(encrtd_word_2.decode('utf-8'))
print(encrtd_word_3.decode('utf-8'))
print(encrtd_word_4.decode('utf-8'))



































