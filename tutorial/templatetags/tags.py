from django import template


register = template.Library()

@register.filter
def indexto(ali, i):
    return ali[:i]



@register.filter
def vaqt(time):
    from datetime import datetime
    now = str(datetime.now())
    print(now)
    x = now.split()[0].split('-')
    z = now.split()[-1].split(':')
    y = int(x[0])
    mo = int(x[1])
    d = int(x[-1])
    h = int(z[0])
    m = int(z[1])
    s = int(z[-1].split('.')[0])
    # request time

    time = str(time)
    tx = time.split()[0].split('-')
    tz = time.split()[-1].split(':')
    ty = int(tx[0])
    tmo = int(tx[1])
    td = int(tx[-1])
    th = int(tz[0])+5
    tm = int(tz[1])
    ts = int(tz[-1].split('.')[0])

    year = y-ty
    mounth = mo-tmo
    day = d-td
    hour = h-th
    minut = m-tm

    time = f"{s-ts} soniya"
    if minut:
        time = f"{m-tm} daqiqa"
    if hour:
        time = f"{h-th} soat"
    if day:
        time = f"{d-td} kun"
    if mounth:
        time = f"{mo-tmo} oy"
    if year:
        time = f"{y-ty} yil"
    return time