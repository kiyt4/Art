
from django import template


register = template.Library()

@register.filter(name='isexistincart')
def isexistincart(products,cart):
    keys= cart.keys()
    print(keys)
    for id in keys:
        if int(id)== products.id:
            return True
    return False
@register.filter(name="cartquantity")
def cartquantity(products,cart):
    keys= cart.keys()
    print(keys)
    for id in keys:
        if int(id)== products.id:
            return cart.get(id)
    return False


@register.filter(name="totalprice")
def totalprice(products,cart):
    return products.price * cartquantity(products,cart)


@register.filter(name="grandtotal")
def grandtotal(products,cart):
    sum =0
    for p in products:
        sum += totalprice(p,cart)
    return sum