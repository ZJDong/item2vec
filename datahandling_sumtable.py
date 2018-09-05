#
YES_SMALL_SONG_H = "./dataset/yes_small/song_hash.txt"
YES_I2V_TAGS = "./dataset/yes_i2v/tags.txt"

#
YES_I2V_SUM = "./dataset/yes_i2v/summary.txt"

f_w = open(YES_I2V_SUM, mode='a+')

with open(YES_SMALL_SONG_H, mode='r') as f_r_1:
    lines = f_r_1.readlines()
    with open(YES_I2V_TAGS, mode='r') as f_r_2:
        for line in lines:
            f_w.write(line[:-1] + "\t")
            f_w.write(f_r_2.readline())

f_w.close()