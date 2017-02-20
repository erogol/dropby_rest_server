"""
How to use Decorators:

Decorators are functions called by annotations
Annotations are the tags prefixed by @
"""

### Decorator functions ###
def helloSpace(target_func):
    def new_func():
        print "Hello Space!"
        target_func()
    return new_func

def helloCosmos(target_func):
    def  new_func():
        print "Hello Cosmos!"
        target_func()
    return new_func


@helloCosmos # annotation
@helloSpace # annotation
def hello():
    print "Hello World!"

### Above code is equivalent to these lines
# hello = helloSpace(hello)
# hello = helloCosmos(hello)

### Let's Try
hello()
