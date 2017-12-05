from re import sub, subn

write_file = open('resources/training_set_tweets_clean.txt', 'w', encoding='utf8')
with open('resources/training_set_tweets.txt', 'r', encoding='utf8') as read_file:
    s = None
    for line in read_file.read().splitlines():
        line = sub(r'\d+\s+\d+\s+', '', line)
        line, n = subn(r'\s+\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}', '', line)
        if s is None:
            s = line
        else:
            s += ' ' + line
        if n > 0:
            write_file.write(s + '\n')
            s = None

write_file.close()
