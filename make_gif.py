import os
import imageio
from a2c_ppo_acktr.multi_agent.utils import save_gif


def main(path):
    images = []
    filenames = list(filter(lambda x: x[-4:] == ".png", list(os.listdir(path))))
    numbers = sorted(list(map(lambda x: int(x[:-4]), filenames)))
    print("Total pngs:", len(numbers))
    for i in numbers:
        filename = "{}.png".format(i)
        im = imageio.imread(os.path.join(path, filename))
        images.append(im)
    save_gif(images, os.path.join(path, "final.gif"), 15)


if __name__ == "__main__":
    main("./sync-results/stag-hunt-gw/no-fruit/2021-03-02T17:19:31.561786/0/ppo/ref-0")
