

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if friend_name:
        return "Hello, {}!".format(friend_name)
    else:
        print "Hello, World!" #weird requirement?
