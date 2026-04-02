def red(text):
    text = '\033[31m' + text + '\033[0m'
    return text


def blue(text):
    text = '\033[34m' + text + '\033[0m'
    return text


def green(text):
    text = '\033[32m' + text + '\033[0m'
    return text


def yellow(text):
    text = '\033[33m' + text + '\033[0m'
    return text


def orange(text):
    text = '\033[38;5;214m' + text + '\033[0m'
    return text


def purple(text):
    text = '\033[35m' + text + '\033[0m'
    return text


def pink(text):
    text = '\033[38;5;212m' + text + '\033[0m'
    return text

print(red('This text should be Red'))
print(blue('This text should be Blue'))
print(green('This text should be Green'))
print(yellow('This text should be Yellow'))
print(orange('This text should be Orange'))
print(purple('This text should be Purple'))
print(pink('This text should be Pink'))