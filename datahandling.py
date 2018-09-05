#
YES_SMALL_TRAIN = "./dataset/yes_small/train.txt"
YES_SMALL_TEST = "./dataset/yes_small/test.txt"

#
YES_I2V = "./dataset/yes_i2v/train.txt"
YES_I2V_2 = "./dataset/yes_i2v/train2.txt"


f_w = open(file=YES_I2V, mode='a+')
f_w_2 = open(file=YES_I2V_2, mode='a+')


def main():
    # Step 1  Combining data sets
    with open(file=YES_SMALL_TRAIN, mode='r') as f:
        lines = f.readlines()
        del lines[0:2]
        for line in lines:
            f_w.write(line)

    with open(file=YES_SMALL_TEST, mode='r') as f:
        lines = f.readlines()
        del lines[0:2]
        for line in lines:
            f_w.write(line)

    f_w.close()

    # Step 2  Deleting the lines with only one element
    with open(file=YES_I2V, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            if line.count(' ') > 1:
                f_w_2.write(line)

    f_w_2.close()


if __name__ == '__main__':
    main()