input_texts = input().rstrip()
input_texts_with_only_alphabet = ''.join(filter(str.isalpha, input_texts)) #Cach chi lay cac chu cai trong input, khong co dau cham, dau phay, v..v
#tao mot dictionary trong do value: chu cai, key: so luong chu cai do
def check_word(texts):
    word_count = {}
    for word in texts:
        word_count[word] = str.count(texts, word)
    return word_count
#tim chu cai duoc lap lai nhieu nhat trong dictionary da tao
def max_in_dict(word_count_dict):
    max_value = [(value, key) for key, value in word_count_dict.items()] #cach tim chu cai duoc lap lai nhieu nhat
    max_letter = (max(max_value)[1])#cach tim chu cai duoc lap lai nhieu nhat
    return max_letter
letter = max_in_dict(check_word(input_texts_with_only_alphabet.lower()))

def max_in_dict_2(word_count_dict):
    max_value = [(value, key) for key, value in word_count_dict.items()]
    number_of_max_letter = (max(max_value)[0]) #tuong tu ta tim duoc cach tim so lan lap cua chu cai do
    return number_of_max_letter
number_of_letter = max_in_dict_2(check_word(input_texts_with_only_alphabet.lower()))

print(f"('{letter}',{number_of_letter})")