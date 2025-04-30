import matplotlib.pyplot as plt, numpy as np

def show(img, time):
    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(time)
    plt.clf()

def flood_fill(img, x, y):
    a, b = img.shape
    if 0 <= x < a and 0 <= y < b and img[x, y] == 1:
        img[x, y] = 2

        show(img, 0)

        flood_fill(img, x + 1, y)
        flood_fill(img, x - 1, y)
        flood_fill(img, x, y + 1)
        flood_fill(img, x, y - 1)
        return None
    else:
        return img

def flood_fill2(img, coord):
    a, b = img.shape
    for x, y in coord:
        if 0 <= x < a and 0 <= y < b and img[x, y] == 1:
            img[x, y] = 2
            show(img, 0)

            coord.append((x + 1, y))
            coord.append((x - 1, y))
            coord.append((x, y + 1))
            coord.append((x, y - 1))

            # thin walls
            # coord.append((x + 1, y + 1))
            # coord.append((x - 1, y - 1))
            # coord.append((x - 1, y + 1))
            # coord.append((x + 1, y - 1))


            flood_fill2(img, coord)

    else:
        return img



def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill2(img, [(0,0)])



if __name__ == "__main__":
    main()
# import time
#
# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)