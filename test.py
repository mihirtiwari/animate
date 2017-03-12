from noun import Noun
import animate as ani

cat = Noun('cat', './test/cat.png')

objects = [cat]

ani.animate(objects, "cat")
