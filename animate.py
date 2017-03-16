from textblob import TextBlob
import graphic as gp

"""object is a dict and phrase is a string"""
"""
Animates the phrase
"""
def animate(object, phrase):
    sentence = TextBlob(phrase)
    pos = sentence.tags

    gp.display(object)
    # for obj, p in zip(pos, object):
    #     if p[0] == obj.get_name() and p[1] == 'NN':
    #         gp.display(obj)
    #     elif 'VB' in p[1]:
    #         gp.show_action(obj, str(p[0]))

animate("./test/cat.jpg", "cat")
