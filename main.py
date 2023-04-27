from pydub import AudioSegment

prevData = [0, '', 0]

# split audio into segments if it's 9+ hours
print('loading audio segment 1')
soundData1 = AudioSegment.from_file('data/audio.mp3', format="mp3")
# print('loading audio segment 2')
# soundData2 = AudioSegment.from_file('data/audio2.mp3', format="mp3")

print('combining audio')
soundData = soundData1
# soundData = soundData1 + soundData2 (delete line 12 and use this one if you had to split up audio)

print('processing audio..')
with open('times.dat', 'r') as data:
    lines = data.readlines()
    for i, line in enumerate(lines):
        time = (int(line.split(' ')[0].split(':')[0]) * 60 * 60 + int(line.split(' ')[0].split(':')[1]) * 60 + int(line.split(' ')[0].split(':')[2])) * 1000
        name = line.strip(line.split(' ')[0] + ' ').strip('\n')

        if i != 0:
            if i < 10:
                i = '0' + str(i)
            sound = soundData[prevData[0]:time].fade_in(duration=2500).fade_out(duration=2500)
            sound.export('exports/' + str(i) + ' Juice WRLD - ' + prevData[1] + '.mp3', format='mp3')
            print(i, time, name)

        prevData = [time, name, i]

    sound = soundData[prevData[0]:len(soundData)].fade_in(duration=2500).fade_out(duration=2500)
    sound.export('exports/' + (str(len(lines)) if len(lines) > 9 else '0' + str(len(lines))) + ' Juice WRLD - ' + prevData[1] + '.mp3', format='mp3')
