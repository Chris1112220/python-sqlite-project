import greeting

greeting.welcome()

def non_built_in_reverser(word):

    word_list = list(word)
    # print(word_list)

    # for i in range(len(word_list) // 2):
    #     word_list[i], word_list[-i - 1] = word_list[-i - 1], word_list[i]

    backward_list = []
    for i in range(len(word_list)):
        # print(-i)
        # print(word_list[-i-1])
        backward_list += word_list[-i-1]
        print(backward_list)
    new_list = "".join(backward_list)
    return new_list

    

    


result = non_built_in_reverser("hello")
print(result)