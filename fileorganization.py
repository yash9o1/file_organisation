import os
# os.rename()
files = os.listdir("C:\\Users\\yasht\\PycharmProjects\\file organization")
i=100
for file in files:
    if file.endswith('.png'):
        os.rename(f"C:\\Users\\yasht\\PycharmProjects\\file organization/{file}", f"C:\\Users\\yasht\\PycharmProjects\\file organization/{i}.png")
        i+=1
        print(file)
