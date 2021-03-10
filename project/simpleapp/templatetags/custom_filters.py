from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то
# django никогда не узнает где именно их искать и фильтры потеряются(


@register.filter(name='multiply') # регестрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргуменит — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg # возвращаемое функцией значение — это то значение, которой подставится к нам в шаблон