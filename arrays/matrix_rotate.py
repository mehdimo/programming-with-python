
# @LearnUpwards
# Rotate a Matrix 90 degrees

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def rotate(M):
    M.reverse()
    for i in range(len(M)):
        for j in range(i):
            M[i][j], M[j][i] = M[j][i], M[i][j]

if __name__ == "__main__":
    image = mpimg.imread("digit-8.png")
    # convert numpy array of image to list
    img_list = image.tolist()
    # show original image
    plt.imshow(img_list)
    plt.show()

    rotate(img_list)
    # show rotated image
    plt.imshow(img_list)
    plt.show()
