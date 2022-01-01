import pafy

file = open('list.txt', 'r')

print("\nDownloader Youtube MP3")
print("======================")

line_count = 0
for line in file:
    if line != "\n":
        line_count += 1

file.close()
file = open('list.txt', 'r')

index = 1
for line in file:
    url = line

    try:
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        print(f"[{index}/{line_count}] " + video.title)

        print(" >> Installing..")
        bestaudio.download(f'{video.title}.mp3')
        # bestaudio.download()

        print(" >> Successfully installed")

        index += 1

    except:
        pass

print("======================")

file.close()
