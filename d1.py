input = open("d1.txt","r")
part = 2

match part: 
    case 1:
        number_list = []

        for line in input:
            line_digits = []
            for character in line:
                if character.isnumeric():
                    line_digits.append(character)
            
            number_list.append(int(line_digits[0] + line_digits[-1]))

        print(sum(number_list))

    case 2:
        number_list = []
        num_dic = {"one":1, "two":2, "three":3, "four":4, "five":5,
                    "six":6, "seven":7, "eight":8, "nine":9}

        for line in input:
            line_digits = []
            for character in range(0,len(line)):
                if line[character].isnumeric():
                    line_digits.append(line[character])
                else:
                    for key,val in num_dic.items():
                        if line[character:character+len(key)] == key:
                            line_digits.append(str(val))

            
            number_list.append(int(line_digits[0] + line_digits[-1]))

        print(sum(number_list))
