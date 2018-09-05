#
YES_SMALL_TAGS = "./dataset/yes_small/tags.txt"

#
YES_I2V_TAGS = "./dataset/yes_i2v/tags.txt"

f_w = open(YES_I2V_TAGS, mode='a+')

with open(YES_SMALL_TAGS, mode='r') as f_r:
    lines = f_r.readlines()
    for line in lines:
        if "#" in line:
            f_w.write('250\n')
        else:
            f_w.write(line)

f_w.close()
