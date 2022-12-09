from django import template

register = template.Library()

words_censor = ['очень', 'плохое', 'слово', 'shit']

@register.filter()
def censor(value):
    for word in words_censor:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value