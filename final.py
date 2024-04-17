from bottle import run, route, template,request,response
import random
import string
import hashlib
import sqlite3
import os
# import pywhatkit as kit
import time
from datetime import timedelta
import datetime
# import pyautogui
import sqlite3
common=None
dic = []
weight=None
sr=None
i=0
image=None
email=None
value=None
flag=None
customer=None
date=None
location=None
number=None
cake=None
amount=None
@route('/orders')
def orders():

    return template('owner_login',dic=dic)
@route('/products')
def products():
    return template('products')
@route('/thankyou')
def thank():
    return template('thank')
@route('/online')
def online():
    return template('online')

@route('/placeorder', method='POST')
def place():
    global weight
    kilo=request.forms.get('kilo')
    weight=kilo
    order=request.forms.get('put')
    if order=='p1':

        return template('logpage', message='')
@route('/occassion')
def occasion():
    return template('occassion')

@route('/place')
def plac():
    return template('place')
@route('/search', method='POST')
def search():
    searchst=request.forms.get('search')
    complete=request.forms.get('done')
    if (searchst=="Cakes" or searchst=="Cake" or searchst=="cakes" or searchst=="cake") and complete=="ai":
        return cakes()
    elif (searchst=="Pastry" or searchst=="Pastries" or searchst=="pastry" or searchst=="pastries")  and complete=="ai":
        return pes()
    elif (searchst == "donut" or searchst == "Donut" or searchst == "donuts" or searchst == "Donuts") and complete == "ai":
        return donut()
    elif (searchst=="Cookies" or searchst=="Cookie" or searchst=="cookies" or searchst=="cookie")  and complete=="ai":
        return cookies()
    elif (searchst=="Chocos" or searchst=="Choco" or searchst=="chocos" or searchst=="choco" or searchst=="chocolates" or searchst=="Chocolates" or searchst=="Chocolate" or searchst=="chocolate" )  and complete=="ai":
        return chocos()

@route('/...', method='POST')
def contact():
    butt=request.forms.get('butt')
    if butt=="log1":
        return products()
    elif butt=="log2":
        return cakes()
    elif butt=="log3":
        return help()
    elif butt=="log5":
        return template('logpage', message="")

@route('/click', method='POST')
def click():
    button_click=request.forms.get('button_clicked')
    if button_click=='b1':
        return occasion()
    elif button_click=='b2':
        return pes()
    elif button_click=='b3':
        return cookies()
    elif button_click=='b4':
        return donut()
    elif button_click=='b5':
        return chocos()
    elif button_click=='b6':
        return many()
@route('/products/login')
def login():
    return template('login')
@route('/logpage')
def logpage():
    return template('logpage', message="")
@route('/products/login/signin')
def signin():
    return template('signin')
@route('/products/cakes')
def cakes():
    return template('cakes')
@route('/products/chocos')
def chocos():
    return template('chocos')
@route('/products/cookies')
def cookies():
    return template('cookies')
@route('/donut')
def donut():
    return template('donut')
@route('/products/many')
def many():
    return template('many')
@route('/products/pes')
def pes():
    return template('pes')
@route('/products/help')
def help():
    return template('help')
@route('/products/pop')
def pop():
    return template('pop')

@route('/buy')
def buy():
    image_source = "none"
    data="none"
    name="none"
    return template('buy',image_source=image_source,prize=data,name=name)


@route('/*buy',method="POST")
def hbuy():
    global cake
    global value
    global flag
    name="none"
    image_source ="none"
    data="none"
    buttons= request.forms.get('button')
    if buttons== 'b1':
        name = " Vanilla Cake"
        data="₹400"
        cake = name
        image_source="https://gurgaonbakers.com/wp-content/uploads/2020/10/classic-love-cake.jpg"
        return template('buy',source=image_source,prize=data,name=name)
    elif buttons == 'b2':
        name = "Butterscotch Cake"
        data = "₹400"
        cake = name
        image_source ="https://www.madbakers.in/cdn/shop/files/half_kg_butterscotch_delight.webp?v=1700667492&width=1946"
        return template('buy',source=image_source,prize=data,name=name)
    elif buttons== 'b3':
        name = "Rasamalai Cake"
        data = "₹600"
        cake = name
        image_source = "https://cakeconnection.in/wp-content/uploads/2020/07/1593768648.rasmalai-cake-450.jpg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b4':
        name = "Rainbow Cake"
        data = "₹600"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToMCjBF1OTbFbIrNbo9k6o4B747Mez1-H0AA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b5':
        name = "Coffee Cake"
        data = "₹500"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRIBGlkc5985HbaiLtGF-IUuk_7InDyZi0ZTJJwBoX7kOY2a1pzUy5cRxs0zFwX-u26fc&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b6':
        name = "Dryfruits Cake"
        data = "₹500"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfpryr_wFqy34cp67D-hVbMevEYHLDNvfyXA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b7':
        name = "Strawberry Cake"
        data = "₹500"
        cake = name
        image_source = "https://mrbrownbakery.com/public/image/images/WgjBaqzqyCo4XVVLHTorCX7R6TJ0j9B6KVjwjjDA.jpeg?p=med"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b8':
        name = "Plainbase dryfruits Cake"
        data = "₹300"
        cake = name
        image_source = "https://www.fnp.com/images/pr/l/v20221201185704/mixed-fruit-delicious-dry-cake-500gms_1.jpg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b9':
        name = "Chocolate Cake"
        data = "₹500"
        cake = name
        image_source = "https://www.tarteletteblog.com/wp-content/uploads/2023/08/cake-flavors-scaled.jpeg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b10':
        name = "Chocolate Cake"
        data = "₹500"
        cake = name
        image_source = "https://d3cif2hu95s88v.cloudfront.net/live-site-2016/product-image/IMG/1601380698cake-350x350.jpeg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b11':
        name = "Blackforest Cake"
        data = "₹500"
        cake = name
        image_source = "https://img.freepik.com/premium-photo/chocolate-cake-with-chocolate-icing-chocolate-drizzles_835197-244.jpg?size=626&ext=jpg&ga=GA1.1.1865367075.1702033247&semt=ais"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b12':
        name = "Cartoon Cake"
        data = "₹500"
        cake = name
        image_source = "https://www.fnp.com/images/pr/l/v20200901172412/sweet-cat-design-cake-chocolate-1-kg_1.jpg"
        return template('buy', source=image_source,prize=data,name=name)

    elif buttons== 'b13':
        name = "Dark Chocolate Pastry"
        data = "₹70"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8EegDAnOVphYD35t-M6b5jp1dJFzn6Otr6A&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b14':
        name = "Butterscotch Pastry"

        data = "₹35"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW_B-cVqIsMCLzIPNexxGMIiRrUlnp8wYIoA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b15':
        name = "Redvelvet Pastry"
        data = "₹90"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg0cREzfriZkAn73CRqeLhhr2zdTPpRZ3htg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b16':
        name = "Chocolate Pastry"
        data = "₹75"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTluNBcHBL3XzB-RtmnQhPDtFncgYgrPsViKoWcOqsoQA8HLj2kSn8JpmCqbuENoAkkMnY&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b17':
        name = "Fruit Pastry"
        data = "₹115"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHVn7tkyK_4PlVOrzyosKY_J5Ukjq9x2GQ4A&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b18':
        name = "Rainbow Pastry"
        data = "₹55"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS295VkwQgCHVoUfJWYIF-VuUiEXp8FQJU8xQ&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b19':
        name = "Whiteforest Pastry"
        data = "₹60"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQplSDUTBafP9jYVkVVkd6Acihj_OkabqRfFA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b20':
        name = "Mixfruit Pastry"
        data = "₹125"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaexYjT8Kx9V-yQ44221hZGCVDxq3KdBYBTQ&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b21':
        name = "Blueberry Pastry"
        data = "₹40"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_NwBPRFoB24C9Fqn30gyhXU1DeWLLIY_zTp9dVSPvJ_d_oMgzUjcCn6OSERNX0RgJT3Y&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b22':
        name = "Mango Pastry"
        data = "₹35"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ0Hh7ae2W6hjP8sZLjGO3R5F853OjwgZQmEM72x0ybZS-SH6dspT2wrt57UtJGcdG82Q&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b23':
        name = "Blackforest Pastry"
        data = "₹65"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4oU3bEjjG2NyM6pHXjwBG7gv6jeJ6LzVK9w&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons== 'b24':
        name = "Orange Pastry"
        data = "₹35"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzmyHvbcwWpShPCjdv7YDlzbbdMVD11Mp5tw&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)

    elif buttons == 'b25':
        name = "Redvelvet Cookies"
        data = "₹399"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn2CepMKywk3hR1SdJD2EGZTZEG2jROV5kxA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b26':
        name = "Oats Cookies"
        data = "₹400"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIkohflrZexNEMXClOtPZrm9iG9EKvB2Q6Mg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b27':
        name = "Coconut Cookies"
        data = "₹400"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWZ94K1lQZhkNJszGw2aAEtPAe4LKoxo-dRA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b28':
        name = "Chocochip Cookies"
        data = "₹450"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-OkvcGrCz987kcvu9DMbwoMf0pjCKO777oA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b29':
        name = "Pinwheel Cookies"
        data = "₹350"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3FouTIqIX-I46djNvIkiMuRbQcLw38mbQ8Q&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b30':
        name = "Nankatai Cookies"
        data = "₹300"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvXMIfEyiF4GD1Du2qjUueu4PGNUC1q3sE6Q&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b31':
        name = "Butter Cookies"
        data = "₹400"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkcq4iw1sqdKEAET0rqnrtmIRRF7lRNDna2Q&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b32':
        name = "Neapolitan Cookies"
        data = "₹500"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9j18w7ESEwFO8zUYagehIwobSQtFFwplTmg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b33':
        name = "Redvelvet Cookies"
        data = "₹399"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjHVaC7RX7JOiqZuWlD97WlB84HZmlWNsHjaJQhNICRDOyAcbIvBNo_hF8eAgOMhKD9E0&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b34':
        name = "Vanilla Chocochip Cookies"
        data = "₹450"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKTE8tQBCcwCue3T_Z39lCtH18gBCafgpPww&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b35':
        name = "Coconut chocolate pinwheel Cookies"
        data = "₹600"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlpN4ySAYECHqDnz_T2iS-D88TVJGJRYHcYIfeMuUKXCj6jowc3391cAcL-P7qKnyApYw&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b36':
        name = "Dark Chocochip Cookies"
        data = "₹650"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlB50xAcy4ZMx8vcYKQj90kETLZBi70q229A&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)

    elif buttons == 'b37':
        name = "Butter Toffee Latte Donut"
        data = "₹70"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc6wzKG-4UgnDiPFmVwsE_5j5qrW3MroQ4gA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b38':
        name = "Cinnamon Donut"
        data = "₹89"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxKzBy-BELQEeTF8kj1xEyoFqUF1yq8Bvltg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b39':
        name = "Vanilla cake Donut"
        data = "₹50"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrfT7J1Bo09CFsLOv63TWESgeD7uZjB5FQPQ&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b40':
        name = "White sugar coated Donut"
        data = "₹75"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOPpKLu9ldmx18725m2-Xw31ckXXDMbkyfbIYNC7Mgwc55N8tWslqgFCi_UErxWbUy4sc&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b41':
        name = "Dark Chocolate Donut"
        data = "₹100"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr2r3jJAx9qnZwKNKkmq3ax70CnDTGS_lata4r_pCVlyTY3owvbzbaMua_kXGrQp0lib4&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b42':
        name = "Redvelet Donut"
        data = "₹75"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFhj6QHbmw4fGlbBcluOnvv6YW-EQcJUyMhH5lnpHzfNiSjGYIls0kYdSgUh6uJ9mSE8I&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b43':
        name = "Hazelnut Bites Donut"
        data = "₹125"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTytibAOSwjNCtHKW47JjZ4tz8WpUeI3SPdng&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b44':
        name = "Krispy Kreme Donut"
        data = "₹150"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKNdS40oC1iz4gYQ0t1xImNgjp_0Df5XtreK5rPXOw_fAd6-TeVgl3SLIscRwsdJgJ590&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b45':
        name = "Lotus Donut"
        data = "₹500"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiArXLH_J6cjME5P9hvgyguO-tk-philfrDg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b46':
        name = "White Chocolate Donut"
        data = "₹65"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCAyl0msG65hfvAwESXd_d2FLQxJ6pAmJgVRdeAVKm1X43uASf1Ll5QeGVu9Qvyfmgf_o&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b47':
        name = "Glaze Donut"
        data = "₹50"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmGBMgYWH17XE31xyVdpAn6pU9_1Pztaov3g&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b48':
        name = "Heart Donut"
        data = "₹500"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEoM6uYm9B3b4RbUn7tqnxF6sUZeSoKt2_RA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)

    elif buttons == 'b49':
        name = "Dark Chocolate"
        data = "₹200"
        cake = name
        image_source = "https://choconnuts.in/wp-content/uploads/2020/07/Coffee-Flavored-Homemade-Chocolate-by-Choco-n-nuts.jpg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b50':
        name = "Chocolate"
        data = "₹150"
        cake = name
        image_source = "https://static.toiimg.com/photo/54407737.cms"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b51':
        name = "Almond coated Chocolate"
        data = "₹700"
        cake = name
        image_source = "https://www.simplyrecipes.com/thmb/05fRqJipRkaBaSSvc_4vJJpGzBc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Homemade-Chocolate-Truffles-LEAD-2-Vertical-3c41c3668ede4d9b8d223fdb0b57fee0.jpg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b52':
        name = "Homemade Chocolate"
        data = "₹200"
        cake = name
        image_source = "https://5.imimg.com/data5/SELLER/Default/2023/11/357891566/ZJ/ZV/DR/36056471/home-made-chocolate-500x500.jpg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b53':
        name = "Nuts Chocolate"
        data = "₹250"
        cake = name
        image_source = "https://www.allrecipes.com/thmb/O3tqcIYOOVONECQLA6uCcuUYcGA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1112044-dc0d53da87d24b10b89e5608777457a0.jpg"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b54':
        name = "Rajbhog Chocolate"
        data = "₹350"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFq2Mukp_GmhBVaNb9pJjvbYHgKVPd6r8m8w&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b55':
        name = "Chocolate Fudge"
        data = "₹350"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn2-S2wBKwOGMuK7eJSPBVPQRsWf2WtMXaMw&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b56':
        name = "Protein Bar"
        data = "₹80"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRop2RH4aqbxQYL7cduQDLqhWHPmmJNqb75Q&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b57':
        name = "Truffle Chocolate"
        data = "₹499"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbDPImv8l_MwTtiGoU0kGudpHXwQkGnjg_GA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b58':
        name = "ButterScotch Chocolate"
        data = "₹250"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXsiIgqLQ0SOLphbvnyE-cbPW3bmnANbPjCupRoDr2m-ZjFZ1wMaEwo8jQHNtlTF7NmDk&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b59':
        name = "Fruit and nut white Chocolate"
        data = "₹455"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTORPBVksVeYNfRNLDzfbf6FUeNcM5CIryfRA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b60':
        name = "White Chocolate Fudge"
        data = "₹250"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZjRYK8EeQjWvYLB9WK5o4N070TJxYMzqUCA&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)

    elif buttons == 'b61':
        name = "Pastel CupCake"
        data = "₹221"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDVWc339cdCezQALDHceTTZ_UAnLfG7LCrOw&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b62':
        name = "Ice Muffin"
        data = "₹175"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnZNfcZiHcZBkoRlwVzNeDfWZoGxEt2xZT5g&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b63':
        name = "Chocolate Hamper"
        data = "₹500"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSznNCppeDV6ZuhAeEfQSS1fVd_sP195QI-Cg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b64':
        name = "Dark Chocolate Hamper"
        data = "₹950"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKeBl8t8CAc-WpIcrRwJ1TfBEF-PTyRB8Kbg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b65':
        name = "Butter Cake"
        data = "₹100"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9aDcWVb-njH6Zq3OBq5WUW88cYs5LjinaVg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b66':
        name = "Gluten Free Bread"
        data = "₹130"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW29qZOzjsgAetw2WhemkvgNwQjMDCXd-CPw&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b67':
        name = "Chocolate Bread"
        data = "₹250"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq9uHwjyvBiMKsBvq01dGo4UsQMt2QLpQUGQ&usqp=CAU&reload=on"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b68':
        name = "Croissant"
        data = "₹169"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9w8uXhoM-NEQAsuuVhg-UUFP0b3fMpIJGBg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b69':
        name = "Veg Puff"
        data = "₹50"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0RNv48Ue3d_EecfZLdP-qwQCvO3buOz3WEX7b08yUhOH6PsvB7So1bKlavYCBRnL-wa0&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b70':
        name = "Paneer Puff"
        data = "₹85"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStZoyup9hu2CoeNpvjLCIUmvf0-B-eJ24PRJulKWnU3UDbujnao7pfdpmC3lVq39WEptU&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b71':
        name = "Dabeli"
        data = "₹25"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiHZm-eH0YGCgA1Eh2FJ8gCaD5io9zAA28jg&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b72':
        name = "Samosa"
        data = "₹15"
        cake = name
        image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5fJiqI_f2N5smbIKiOXC_5N57gE-rf4zJ3w&usqp=CAU"
        return template('buy', source=image_source,prize=data,name=name)
    elif buttons == 'b73':
        if value=='v1':
            if flag=='bt1':
                name = "Doraemon Theme"
                data = "₹500"
                cake = name
                image_source = "https://assets.winni.in/c_limit,dpr_1,fl_progressive,q_80,w_1000/25972_doraemon-cartoon-cake.jpeg"
            elif flag=='bt2':
                name = "Music Theme 1"
                data = "₹400"
                cake = name
                image_source = "https://images-cdn.ubuy.co.in/633ff9fe99fe674fdb257744-24pcs-guitar-cake-toppers-music-note.jpg"
            elif flag=='bt3':
                name='Painting Theme 1'
                data='₹500'
                cake = name
                image_source="https://m.media-amazon.com/images/I/713ZO307HNL.jpg"
            elif flag=='bt4':
                name='Makeup Theme 1'
                data='₹500'
                cake = name
                image_source="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQw2DBC9YCJaP_RGGp25F74jl2ZhYACnSxLIw&usqp=CAU"
            elif flag=='bt5':
                name='Teacher Theme'
                data='₹500'
                cake = name
                image_source="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsJhkFInCLSk4NTan2U-9FgUHo_IYV2A2jEw&usqp=CAU"
            elif flag=='bt6':
                name='Gym Theme'
                data='₹500'
                cake = name
                image_source="https://assets.giftalove.com/resources/common/giftimages/productimage1/bodybuilder-themed-fondant-cake.jpg"
        elif value =='v2':
            name = "Engagement Cake 1"
            data = "₹500"
            cake = name
            image_source = "https://i.pinimg.com/736x/19/3e/64/193e645309dcbfb4130b4d6eb0918c53.jpg"
        elif  value =='v3':
            name = "Baby Shower cake 1"
            data = "₹450"
            cake = name
            image_source = "https://smoor.in/cdn/shop/files/cake_0154_BabyShowerDelightCake_1200x1200.jpg?v=1683609062"
        elif  value =='v4':
            name = "Anniversary cake 1"
            data = "₹450"
            cake = name
            image_source = "https://www.doughandcream.com/wp-content/uploads/2023/04/9-Happy-Wedding-Anniversary-Cake-Images-in-White-for-Pure-Elegance-1.jpeg"

        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b74':
        if value=='v1':
            if flag=='bt1':
                name = "Taddy Theme"
                data = "₹400"
                cake = name
                image_source = "https://www.asansolcake.com/wp-content/uploads/2021/06/panda-cake-1.jpg"
            elif flag=='bt2':
                name = "Music Theme 2"
                data = "₹500"
                cake = name
                image_source = "https://m.media-amazon.com/images/I/71tK6ksOrlL.jpg"
            elif flag=='bt3':
                name = "Painting Theme 2"
                data = "₹500"
                cake = name
                image_source = "https://smoor.in/cdn/shop/files/CustomiseCakeWebsiteImages_0046_The-Artist-Cake_1200x1200.jpg?v=1684319606"
            elif flag=='bt4':
                name = "Makeup Theme 2"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNg-N_H7csLw2kPiQemi-G-u9avLfXFO21fg&usqp=CAU"
            elif flag=='bt5':
                name = "Job Theme"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQph-pfcepF1U216VhX487qWmg8_QMiMYw_dg&usqp=CAU"
            elif flag=='bt6':
                name = "Winning Theme"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtiqDnVAsKrZWnamRlc8OSQev91Us5pSq-pQ&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 2"
            data = "₹500"
            cake = name
            image_source = "https://i0.wp.com/manbhari.co.in/wp-content/uploads/2023/07/1000042997.jpg?fit=2048%2C2048&ssl=1"
        elif value == 'v3':
            name = "Baby Shower cake 2"
            data = "₹450"
            cake = name
            image_source = "https://www.doughandcream.com/wp-content/uploads/2023/04/cake-baby-1.jpeg"
        elif value == 'v4':
            name = "Anniversary cake 2"
            data = "₹500"
            cake = name
            image_source = "https://www.bakingo.com/blog/wp-content/uploads/2020/12/rose-flower-cake.jpg"
        return template('buy', source=image_source, prize=data, name=name)

    elif buttons == 'b75':
        if value=='v1':
            if flag=='bt1':
                name = "Minion"
                data = "₹500"
                cake = name
                image_source = "https://i.pinimg.com/736x/e7/41/1f/e7411f4c46807de3198d1869c89e5e43.jpg"
            elif flag=='bt2':
                name = "Music Theme 3"
                data = "₹500"
                cake = name
                image_source = "https://i.pinimg.com/736x/3b/6d/48/3b6d48851808cdcaacbad20d8dd72de2.jpg"
            elif flag=='bt3':
                name = "Painting Theme 3"
                data = "₹500"
                cake = name
                image_source = "https://cakesburg.co.uk/cdn/shop/products/Painter-cake-22_800x.jpg?v=1642464916"
            elif flag=='bt4':
                name = "Makeup Theme 3"
                data = "₹500"
                cake = name
                image_source = "https://www.yummycake.co.in/wp-content/uploads/2023/03/MAC-Makeup-Theme-Cake.jpg"
            elif flag=='bt5':
                name = "Teacher day"
                data = "₹400"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8AerchnsrkH3cNKhZQcuA2hVXLlK3_BwJbg&usqp=CAU"
            elif flag=='bt6':
                name = "Volleyball"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrRBoWrcS54SCgY9SGZKJSlnXROCeWExHNTA&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 3"
            data = "₹500"
            cake = name
            image_source = "https://smoor.in/cdn/shop/files/WhatsAppImage2023-05-11at2.08.45PM_1200x1200.jpg?v=1683797034"
        elif value == 'v3':
            name = "Baby Shower cake 3"
            data = "₹450"
            cake = name
            image_source = "https://ovenfresh.in/wp-content/uploads/2023/02/Pink-And-Blue-Rosette-Cake-850-Gms-With-A-He-Or-She-Topper.jpg"
        elif value == 'v4':
            name = "Anniversary cake 3"
            data = "₹450"
            cake = name
            image_source = "https://cdn.dotpe.in/longtail/store-items/7695373/4OmEO5hP.jpeg"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b76':
        if value=='v1':
            if flag=='bt1':
                name = "Panda"
                data = "₹500"
                cake = name
                image_source = "https://www.cakeplaza.in/cdn/shop/products/panda-cake_x700.jpg?v=1608191522"
            elif flag=='bt2':
                name = "Music Theme 4"
                data = "₹500"
                cake = name
                image_source = "https://liliyum.com/cdn/shop/files/GrandPianoCake_2400x.jpg?v=1692624194"
            elif flag=='bt3':
                name = "Painting Theme 4"
                data = "₹500"
                cake = name
                image_source = "https://m.media-amazon.com/images/I/715G8wJx8XL.jpg"
            elif flag=='bt4':
                name = "Makeup Theme 4"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY6KhdUyaGPk_DlGkj--6MkYDLXRPRtzqM9A&usqp=CAU"
            elif flag=='bt5':
                name = "Doctor"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoqAoGvAwR8l5I4O60DT06lNllQl-Ygfvn4A&usqp=CAU"
            elif flag=='bt6':
                name = "Cricket"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNw9ZitASIY7EnarZo2rGOOz2c7mKLlux9iQ&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 4"
            data = "₹500"
            cake = name
            image_source = "https://www.cakesandbakes.in/weddingcake/fondant-flower-engagement-cake.jpg"
        elif value == 'v3':
            name = "Baby Shower cake 4"
            data = "₹450"
            cake = name
            image_source = "https://legateaucakes.com/cdn/shop/files/Babyshower1.jpg?v=1705660266&width=1946"
        elif value == 'v4':
            name = "Anniversary cake 4"
            data = "₹500"
            cake = name
            image_source = "https://smoor.in/cdn/shop/files/CustomiseCakeWebsiteImages_0019_BloomingAnniversaryCake_1200x1200.jpg?v=1684389308"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b77':
        if value=='v1':
            if flag=='bt1':
                name = "Shinchan"
                data = "₹500"
                cake = name
                image_source = "https://www.giftmyemotions.com/image/cache/floralnation/cakes/ct5-800x800.jpg"
            elif flag=='bt2':
                name = "Music Theme 5"
                data = "₹500"
                cake = name
                image_source = "https://m.media-amazon.com/images/I/81okbqFFLyL.jpg"
            elif flag=='bt3':
                name = "Painting Theme 4"
                data = "₹500"
                cake = name
                image_source = "https://live.staticflickr.com/8053/8417232675_06048bd47e_c.jpg"
            elif flag=='bt4':
                name = "Makeup Theme 4"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjY6dzU-BK7IsUUyhK3mW2lMIKVEFOG7UBmQ&usqp=CAU"
            elif flag=='bt5':
                name = "Doctor"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIy9ovTf98YHLTSqdEBRkxOTKC8YzZlpmzNg&usqp=CAU"
            elif flag=='bt6':
                name = "Cricket"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu8WE_Z6_RTyB81dB1ScKgMhD-f2yY8FPaeQ&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 5"
            data = "₹500"
            cake = name
            image_source = "https://www.cakesquarechennaionline.com/wp-content/uploads/2023/08/WHITE-AND-GOLD-THEME-WEDDING-CAKE_-ENGAGEMENT-CAKE-63-2.jpg"
        elif value == 'v3':
            name = "Baby Shower cake 5"
            data = "₹450"
            cake = name
            image_source = "https://www.kukkr.com/cdn/shop/products/cradle-baby-shower-cake-kukkr-cakes-2.jpg?v=1678855796&width=416"
        elif value == 'v4':
            name = "Anniversary cake 5"
            data = "₹450"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwd_DWOo0mJqlYXfLw-9oRjbfmwKM-2FTTQw&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b78':
        if value=='v1':
            if flag=='bt1':
                name = "Spider man"
                data = "₹400"
                cake = name
                image_source = "https://www.bettergiftflowers.com/wp-content/uploads/2021/06/spidy-cake-2.jpg"
            elif flag=='bt2':
                name = "Music Theme 5"
                data = "₹500"
                cake = name
                image_source = "https://www.bakehoney.com/media/23321/conversions/27941_08-27-2022_12-08-03_name_000This-Musician-And-Headphone-Cake-is-a-perfect-cake-for-music-lover-banner.jpg"
            elif flag=='bt3':
                name = "Painting Theme 5"
                data = "₹500"
                cake = name
                image_source = "https://i.pinimg.com/originals/a6/b8/7e/a6b87e757075eda9b43a0212228becf7.jpg"
            elif flag=='bt4':
                name = "Makeup Theme 5"
                data = "₹500"
                cake = name
                image_source = "https://www.adultcakes.in/wp-content/uploads/2018/06/makeup-kit-cake-1.jpg"
            elif flag=='bt5':
                name = "Advocate"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUoHqXoZbNsVJbZdeO85EVFeoMCQIiXgVw4A&usqp=CAU"
            elif flag=='bt6':
                name = "Table tennis"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZGq1nwMSZPB6SL4KnyJjNiEISSmCLbnXUbw&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 6"
            data = "₹500"
            cake = name
            image_source = "https://www.cakesquarechennaionline.com/wp-content/uploads/2023/08/Elegant-Engagement-Cake-Premium-cakes.jpg"
        elif value == 'v3':
            name = "Baby Shower cake 6"
            data = "₹450"
            cake = name
            image_source = "https://cakeconnection.in/wp-content/uploads/2021/07/673cba9e-3e55-4646-bc5c-83432407469c.jpg"
        elif value == 'v4':
            name = "Anniversary cake 6"
            data = "₹500"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoMZhLK1Nl8CgQi70CJuN-MLeqeOIM4QOJtg&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b79':
        if value=='v1':
            if flag=='bt1':
                name = "Mickey"
                data = "₹500"
                cake = name
                image_source = "https://levanilla.in/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/0/2/02.jpg"
            elif flag=='bt2':
                name = "Music Theme 7"
                data = "₹500"
                cake = name
                image_source = "https://imgs.classicfm.com/images/14938?crop=16_9&width=660&relax=1&format=webp&signature=lqshG91xh2pz18l8_yfABCHEdrg="
            elif flag=='bt3':
                name = "Painting Theme 7"
                data = "₹500"
                cake = name
                image_source = "https://cakesburg.co.uk/cdn/shop/products/Painting_relaxing_cake_10_800x.jpg?v=1535231450"
            elif flag=='bt4':
                name = "Makeup Theme 7"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTO_9JhQjjsbGQ5S93-fXNOXsKzConCtEWD7w&usqp=CAU"
            elif flag=='bt5':
                name = "Job Theme"
                data = "₹400"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9XVM16-2CQM5tImhEd5D7G2crOXG0S24fAw&usqp=CAU"
            elif flag=='bt6':
                name = "Running"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_8kL6DkWYePoY9rO6h6PgOXJU5981wcoc7Q&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 7"
            data = "₹500"
            cake = name
            image_source = "https://gopalcakewala.com/wp-content/uploads/2022/12/red-and-white-engagement-cake.png"
        elif value == 'v3':
            name = "Baby Shower cake 7"
            data = "₹450"
            cake = name
            image_source = "https://i0.wp.com/cakesmash.in/wp-content/uploads/2022/01/CSBabyShower010.jpg?fit=1080%2C1080&ssl=1"
        elif value == 'v4':
            name = "Anniversary cake 7"
            data = "₹450"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrM5TeQyi8OO8LniUR6zHHENsnwkB4GzSUHQ&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b80':
        if value=='v1':
            if flag=='bt1':
                name = "Dragon ball"
                data = "₹500"
                cake = name
                image_source = "https://cdn.dotpe.in/longtail/store-items/7863693/Mro3v76W.jpeg"
            elif flag=='bt2':
                name = "Music Theme 8"
                data = "₹500"
                cake = name
                image_source = "https://houseofcakesdubai.com/store/image/cache/catalog/10%20photos/cakewithmenfigureandmiusicalmnotes_custom_cakes_dubai_5175-500x500.jpg"
            elif flag=='bt3':
                name = "Painting Theme 8"
                data = "₹500"
                cake = name
                image_source = "https://www.cravebyleena.com/cdn/shop/products/Artlove.png?v=1701592410"
            elif flag=='bt4':
                name = "Makeup Theme 8"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWsHzhazj7dvbo0LyMrKOk899yigfUV_hZLg&usqp=CAU"
            elif flag=='bt5':
                name = "Software Job Theme"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC2PXWiSfrMx5xYS3o2m0XJcrqZc3KOfwiPw&usqp=CAU"
            elif flag=='bt6':
                name = "Football"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjT521KhH9jYueNatB0kyl_gNqYXT7kF75-w&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 8"
            data = "₹500"
            cake = name
            image_source = "https://i0.wp.com/floralxpress.in/wp-content/uploads/2023/02/fxengagement010.jpg?fit=500%2C500&ssl=1"
        elif value == 'v3':
            name = "Baby Shower cake 8"
            data = "₹450"
            cake = name
            image_source = "https://i2.wp.com/cakesmash.in/wp-content/uploads/2022/01/CSBabyShower008.jpg?fit=1080%2C1080&ssl=1"
        elif value == 'v4':
            name = "Anniversary cake 8"
            data = "₹500"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTANWPwOn3LS0mzf0Dk8IruD4AoAUL3eYw4Kg&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b81':
        if value=='v1':
            if flag=='bt1':
                name = "Doraemon"
                data = "₹500"
                cake = name
                image_source = "https://www.sendbestgift.com/assets/images/product/2192f2a1a78c5d263dbd8150825d4b12.jpg"
            elif flag=='bt2':
                name = "Music Theme 9"
                data = "₹500"
                cake = name
                image_source = "https://images-cdn.ubuy.co.in/633ff9fe99fe674fdb257745-24pcs-guitar-cake-toppers-music-note.jpg"
            elif flag=='bt3':
                name = "Painting Theme 9"
                data = "₹500"
                cake = name
                image_source = "https://pic.warmoven.in/catalog/product/cache/4e14bcb566d25893ae7201d4dbdc22fd/image/1340483e/painter-cake.png"
            elif flag=='bt4':
                name = "Makeup Theme 9"
                data = "₹500"
                cake = name
                image_source = "https://www.kanpurgifts.com/admin/product_images/makeup%201.jpg"
            elif flag=='bt5':
                name = "Teacher Theme"
                data = "₹400"
                cake = name
                image_source = "https://www.thecaker.com/cdn/shop/products/School_theme_cake_1024x1024.jpg?v=1569680816"
            elif flag=='bt6':
                name = "Golf game"
                data = "₹450"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe8SIAG9AUD9b7KZ3K34dQpFAbkuQlt9wunA&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 9"
            data = "₹500"
            cake = name
            image_source = "https://www.deliciaecakes.com/static/f0ae777bfd58608ba300bd2d1af88c92/0f3a1/w-455.jpg"
        elif value == 'v3':
            name = "Baby Shower cake 9"
            data = "₹450"
            cake = name
            image_source = "https://shop.aubree.in/cdn/shop/products/ElephantBabyShowerCake_6451eeb6-e618-4181-a277-2382a28e04a3_1024x1024.jpg?v=1655967042"
        elif value == 'v4':
            name = "Anniversary cake 9"
            data = "₹450"
            cake = name
            image_source = "https://i2.wp.com/cakesmash.in/wp-content/uploads/2021/12/CSAnniversary009.jpg?fit=1080%2C1080&ssl=1"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b82':
        if value=='v1':
            if flag=='bt1':
                name = "Cocomelon"
                data = "₹500"
                cake = name
                image_source = "https://yummycake.in/wp-content/uploads/2022/06/cocomelon-cartoon-cake.png"
            elif flag=='bt2':
                name = "Music Theme 10"
                data = "₹500"
                cake = name
                image_source = "https://houseofcakesdubai.com/store/image/cache/catalog/8%20photos/DSC_8684-500x500.jpg"
            elif flag=='bt3':
                name = "Painting Theme 10"
                data = "₹500"
                cake = name
                image_source = "https://i.pinimg.com/originals/71/03/8d/71038dd5635c97305bceeb48486f1156.jpg"
            elif flag=='bt4':
                name = "Makeup Theme 10"
                data = "₹500"
                cake = name
                image_source = "https://www.cakeplaza.in/cdn/shop/products/Mac_x700.jpg?v=1611921003"
            elif flag=='bt5':
                name = "Youtube Theme"
                data = "₹450"
                cake = name
                image_source = "https://www.chefrajanbakery.com/uploads_drop/1695220639Image-5514.jpg"
            elif flag=='bt6':
                name = "Football"
                data = "₹500"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDpaL0nn5-PWkV76Q2ulDEvp1sJ1BGKJ0YYyzTLOL-PbKpTO3ZaJLgRtUsngmrzYWQ5Js&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 10"
            data = "₹500"
            cake = name
            image_source = "https://i0.wp.com/floralxpress.in/wp-content/uploads/2023/02/fxengagement011.jpg?fit=658%2C657&ssl=1"
        elif value == 'v3':
            name = "Baby Shower cake 10"
            data = "₹450"
            cake = name
            image_source = "https://www.thecake.in/image/cache/catalog/cake/baby-shower-cake-from-TheCake%20copy%20(1)%20(1)%20(1)-500x500.jpg"
        elif value == 'v4':
            name = "Anniversary cake 10"
            data = "₹500"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzOl8YyZh_-Gj95IrlipBGMYKDDY5uci7pDA&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b83':
        if value=='v1':
            if flag=='bt1':
                name = "Angry bird"
                data = "₹500"
                cake = name
                image_source = "https://www.bakingo.com/blog/wp-content/uploads/2022/02/Popular-Cartoon-Cake-For-Birthday-Celebration.jpg"
            elif flag=='bt2':
                name = "Music Theme 11"
                data = "₹500"
                cake = name
                image_source = "https://s3.amazonaws.com/cdn001.cakecentral.com/gallery/2015/02/900_690230DjO7_grooms-cake-for-a-musician.jpg"
            elif flag=='bt3':
                name = "Painting Theme 12"
                data = "₹500"
                cake = name
                image_source = "https://m.media-amazon.com/images/I/814fqSef8rL.jpg"
            elif flag=='bt4':
                name = "Makeup Theme 12"
                data = "₹500"
                cake = name
                image_source = "https://www.bakehoney.com/media/38948/conversions/33446_12-30-2022_16-38-30_name_000000000000Makeup-Theme-Cake-by-sweet-art-from-bakehoney-banner.jpg"
            elif flag=='bt5':
                name = "Teacher day"
                data = "₹500"
                cake = name
                image_source = "https://i.pinimg.com/originals/ae/50/a5/ae50a503874d756863875147759afa8a.jpg"
            elif flag=='bt6':
                name = "Cricket Theme"
                data = "₹450"
                cake = name
                image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy3UB2urYVZFcw3lEjtoZpZVjB0HAHhUkL3w&usqp=CAU"
        elif value == 'v2':
            name = "Engagement Cake 11"
            data = "₹500"
            cake = name
            image_source = "https://www.tfcakes.in/images/products/221226_023557_705_658.jpg"
        elif value == 'v3':
            name = "Baby Shower cake 11"
            data = "₹450"
            cake = name
            image_source = "https://m.media-amazon.com/images/I/617Oda2VHLL._AC_UF1000,1000_QL80_.jpg"
        elif value == 'v4':
            name = "Anniversary cake 11"
            data = "₹500"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSlBBRnsv2u-vIWmO5Qj8FrhO7wHcU57mPOg&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
    elif buttons == 'b84':
        if value=='v1':
            if flag=='bt1':
                name = "Mickey mouse"
                data = "₹400"
                cake = name
                image_source = "https://cdn-media.indiacakes.com/media/catalog/product/cache/0b945dd31857d9e2e2ef055978ab9981/m/i/mickey-mouse-theme-cake.webp"
            elif flag=='bt2':
                name = "Music Theme 12"
                data = "₹500"
                cake = name
                image_source = "https://d2j6dbq0eux0bg.cloudfront.net/images/62619602/4028877643.png"
            elif flag=='bt3':
                name = "Painting Theme 12"
                data = "₹500"
                cake = name
                image_source = "https://thememyparty.in/cdn/shop/products/CakeTopper_4c19df2f-b729-4951-876b-d85fca3c8dc6_800x.jpg?v=1666934444"
            elif flag=='bt4':
                name = "Makeup Theme 12"
                data = "₹500"
                cake = name
                image_source = "https://www.flavoursguru.com/image/catalog/catimg/primary/makeup-queen.jpg"
            elif flag=='bt5':
                name = "Teacher day Theme"
                data = "₹400"
                cake = name
                image_source = "https://assets.winni.in/product/primary/2021/8/53421.jpeg?dpr=2&w=220"
            elif flag=='bt6':
                name = "Football"
                data = "₹500"
                cake = name
                image_source = "https://i.pinimg.com/736x/d8/1a/67/d81a6770583f8af034c7e22f9a2157d3.jpg"
        elif value == 'v2':
            name = "Engagement Cake 12"
            data = "₹500"
            cake = name
            image_source = "https://www.cakesquarechennaionline.com/wp-content/uploads/2023/08/ELEGANT-ENGAGEMENT-CAKE-1.jpg"
        elif value == 'v3':
            name = "Baby Shower cake 12"
            data = "₹450"
            cake = name
            image_source = "https://liliyum.com/cdn/shop/files/PinkandBlueBabyShowerCake_800x.jpg?v=1689655009"
        elif value == 'v4':
            name = "Anniversary cake 12"
            data = "₹500"
            cake = name
            image_source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvH1z2vSIXiukzxq4y_OcjtjGnHIP3hRTHNVBaW99SyfOZenh4_XxCvtHuDWRiSuKFApI&usqp=CAU"
        return template('buy', source=image_source, prize=data, name=name)
@route('/caketype')
def caketype():
    return template('caketype')
@route('/dynamic')
def dynamic():
    image_source1 = "none"
    image_source2 = "none"
    image_source3 = "none"
    image_source4 = "none"
    image_source5 = "none"
    image_source6 = "none"
    image_source7 = "none"
    image_source8 = "none"
    image_source9 = "none"
    image_source10 = "none"
    image_source11 = "none"
    image_source12 = "none"
    return template('dynamic',text='none', source1=image_source1, source2=image_source2, source3=image_source3,
                    source4=image_source4, source5=image_source5,
                    source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                    source10=image_source10, source11=image_source11, source12=image_source12)
@route('/&&', method='POST')
def clicked():
    global value
    _click=request.forms.get('clicked')
    value=_click
    if _click=='v1':
        return caketype()
    elif _click=='v2':
        image_source1 = "https://i.pinimg.com/736x/19/3e/64/193e645309dcbfb4130b4d6eb0918c53.jpg"
        image_source2 = "https://i0.wp.com/manbhari.co.in/wp-content/uploads/2023/07/1000042997.jpg?fit=2048%2C2048&ssl=1"
        image_source3 = "https://smoor.in/cdn/shop/files/WhatsAppImage2023-05-11at2.08.45PM_1200x1200.jpg?v=1683797034"
        image_source4 = "https://www.cakesandbakes.in/weddingcake/fondant-flower-engagement-cake.jpg"
        image_source5 = "https://www.cakesquarechennaionline.com/wp-content/uploads/2023/08/WHITE-AND-GOLD-THEME-WEDDING-CAKE_-ENGAGEMENT-CAKE-63-2.jpg"
        image_source6 = "https://www.cakesquarechennaionline.com/wp-content/uploads/2023/08/Elegant-Engagement-Cake-Premium-cakes.jpg"
        image_source7 = "https://gopalcakewala.com/wp-content/uploads/2022/12/red-and-white-engagement-cake.png"
        image_source8 = "https://i0.wp.com/floralxpress.in/wp-content/uploads/2023/02/fxengagement010.jpg?fit=500%2C500&ssl=1"
        image_source9 = "https://www.deliciaecakes.com/static/f0ae777bfd58608ba300bd2d1af88c92/0f3a1/w-455.jpg"
        image_source10 = "https://i0.wp.com/floralxpress.in/wp-content/uploads/2023/02/fxengagement011.jpg?fit=658%2C657&ssl=1"
        image_source11 = "https://www.tfcakes.in/images/products/221226_023557_705_658.jpg"
        image_source12 = "https://www.cakesquarechennaionline.com/wp-content/uploads/2023/08/ELEGANT-ENGAGEMENT-CAKE-1.jpg"
        return template('dynamic',text='Engagement Cakes', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)


    elif _click=='v3':
        image_source1 = "https://smoor.in/cdn/shop/files/cake_0154_BabyShowerDelightCake_1200x1200.jpg?v=1683609062"
        image_source2 = "https://www.doughandcream.com/wp-content/uploads/2023/04/cake-baby-1.jpeg"
        image_source3 = "https://ovenfresh.in/wp-content/uploads/2023/02/Pink-And-Blue-Rosette-Cake-850-Gms-With-A-He-Or-She-Topper.jpg"
        image_source4 = "https://legateaucakes.com/cdn/shop/files/Babyshower1.jpg?v=1705660266&width=1946"
        image_source5 = "https://www.kukkr.com/cdn/shop/products/cradle-baby-shower-cake-kukkr-cakes-2.jpg?v=1678855796&width=416"
        image_source6 = "https://cakeconnection.in/wp-content/uploads/2021/07/673cba9e-3e55-4646-bc5c-83432407469c.jpg"
        image_source7 = "https://i0.wp.com/cakesmash.in/wp-content/uploads/2022/01/CSBabyShower010.jpg?fit=1080%2C1080&ssl=1"
        image_source8 = "https://i2.wp.com/cakesmash.in/wp-content/uploads/2022/01/CSBabyShower008.jpg?fit=1080%2C1080&ssl=1"
        image_source9 = "https://shop.aubree.in/cdn/shop/products/ElephantBabyShowerCake_6451eeb6-e618-4181-a277-2382a28e04a3_1024x1024.jpg?v=1655967042"
        image_source10 = "https://www.thecake.in/image/cache/catalog/cake/baby-shower-cake-from-TheCake%20copy%20(1)%20(1)%20(1)-500x500.jpg"
        image_source11 = "https://m.media-amazon.com/images/I/617Oda2VHLL._AC_UF1000,1000_QL80_.jpg"
        image_source12 = "https://liliyum.com/cdn/shop/files/PinkandBlueBabyShowerCake_800x.jpg?v=1689655009"
        return template('dynamic',text='Baby Shower', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)

    elif _click=='v4':
        image_source1 = "https://www.doughandcream.com/wp-content/uploads/2023/04/9-Happy-Wedding-Anniversary-Cake-Images-in-White-for-Pure-Elegance-1.jpeg"
        image_source2 = "https://www.bakingo.com/blog/wp-content/uploads/2020/12/rose-flower-cake.jpg"
        image_source3 = "https://cdn.dotpe.in/longtail/store-items/7695373/4OmEO5hP.jpeg"
        image_source4 = "https://smoor.in/cdn/shop/files/CustomiseCakeWebsiteImages_0019_BloomingAnniversaryCake_1200x1200.jpg?v=1684389308"
        image_source5 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwd_DWOo0mJqlYXfLw-9oRjbfmwKM-2FTTQw&usqp=CAU"
        image_source6 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoMZhLK1Nl8CgQi70CJuN-MLeqeOIM4QOJtg&usqp=CAU"
        image_source7 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrM5TeQyi8OO8LniUR6zHHENsnwkB4GzSUHQ&usqp=CAU"
        image_source8 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTANWPwOn3LS0mzf0Dk8IruD4AoAUL3eYw4Kg&usqp=CAU"
        image_source9 = "https://i2.wp.com/cakesmash.in/wp-content/uploads/2021/12/CSAnniversary009.jpg?fit=1080%2C1080&ssl=1"
        image_source10 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzOl8YyZh_-Gj95IrlipBGMYKDDY5uci7pDA&usqp=CAU"
        image_source11 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSlBBRnsv2u-vIWmO5Qj8FrhO7wHcU57mPOg&usqp=CAU"
        image_source12 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvH1z2vSIXiukzxq4y_OcjtjGnHIP3hRTHNVBaW99SyfOZenh4_XxCvtHuDWRiSuKFApI&usqp=CAU"
        return template('dynamic',text='Anniversary', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)

@route('/&*', method='POST')
def clicked():
    global flag
    _click=request.forms.get('buttons')
    flag=_click
    if _click=='bt1':
        image_source1 = "https://assets.winni.in/c_limit,dpr_1,fl_progressive,q_80,w_1000/25972_doraemon-cartoon-cake.jpeg"
        image_source2 = "https://www.asansolcake.com/wp-content/uploads/2021/06/panda-cake-1.jpg"
        image_source3 = "https://i.pinimg.com/736x/e7/41/1f/e7411f4c46807de3198d1869c89e5e43.jpg"
        image_source4 = "https://www.cakeplaza.in/cdn/shop/products/panda-cake_x700.jpg?v=1608191522"
        image_source5 = "https://www.giftmyemotions.com/image/cache/floralnation/cakes/ct5-800x800.jpg"
        image_source6 = "https://www.bettergiftflowers.com/wp-content/uploads/2021/06/spidy-cake-2.jpg"
        image_source7 = "https://levanilla.in/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/0/2/02.jpg"
        image_source8 = "https://cdn.dotpe.in/longtail/store-items/7863693/Mro3v76W.jpeg"
        image_source9 = "https://www.sendbestgift.com/assets/images/product/2192f2a1a78c5d263dbd8150825d4b12.jpg"
        image_source10 = "https://yummycake.in/wp-content/uploads/2022/06/cocomelon-cartoon-cake.png"
        image_source11 = "https://www.bakingo.com/blog/wp-content/uploads/2022/02/Popular-Cartoon-Cake-For-Birthday-Celebration.jpg"
        image_source12 = "https://cdn-media.indiacakes.com/media/catalog/product/cache/0b945dd31857d9e2e2ef055978ab9981/m/i/mickey-mouse-theme-cake.webp"
        return template('dynamic', text='Engagement Cakes', source1=image_source1, source2=image_source2,
                        source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)

    elif _click=='bt2':
        image_source1 = "https://images-cdn.ubuy.co.in/633ff9fe99fe674fdb257744-24pcs-guitar-cake-toppers-music-note.jpg"
        image_source2 = "https://m.media-amazon.com/images/I/71tK6ksOrlL.jpg"
        image_source3 = "https://i.pinimg.com/736x/3b/6d/48/3b6d48851808cdcaacbad20d8dd72de2.jpg"
        image_source4 = "https://liliyum.com/cdn/shop/files/GrandPianoCake_2400x.jpg?v=1692624194"
        image_source5 = "https://m.media-amazon.com/images/I/81okbqFFLyL.jpg"
        image_source6 = "https://www.bakehoney.com/media/23321/conversions/27941_08-27-2022_12-08-03_name_000This-Musician-And-Headphone-Cake-is-a-perfect-cake-for-music-lover-banner.jpg"
        image_source7 = "https://imgs.classicfm.com/images/14938?crop=16_9&width=660&relax=1&format=webp&signature=lqshG91xh2pz18l8_yfABCHEdrg="
        image_source8 = "https://houseofcakesdubai.com/store/image/cache/catalog/10%20photos/cakewithmenfigureandmiusicalmnotes_custom_cakes_dubai_5175-500x500.jpg"
        image_source9 = "https://images-cdn.ubuy.co.in/633ff9fe99fe674fdb257745-24pcs-guitar-cake-toppers-music-note.jpg"
        image_source10 = "https://houseofcakesdubai.com/store/image/cache/catalog/8%20photos/DSC_8684-500x500.jpg"
        image_source11 = "https://s3.amazonaws.com/cdn001.cakecentral.com/gallery/2015/02/900_690230DjO7_grooms-cake-for-a-musician.jpg"
        image_source12 = "https://d2j6dbq0eux0bg.cloudfront.net/images/62619602/4028877643.png"
        return template('dynamic',text='Engagement Cakes', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)


    elif _click=='bt3':
        image_source1 = "https://m.media-amazon.com/images/I/713ZO307HNL.jpg"
        image_source2 = "https://smoor.in/cdn/shop/files/CustomiseCakeWebsiteImages_0046_The-Artist-Cake_1200x1200.jpg?v=1684319606"
        image_source3 = "https://cakesburg.co.uk/cdn/shop/products/Painter-cake-22_800x.jpg?v=1642464916"
        image_source4 = "https://m.media-amazon.com/images/I/715G8wJx8XL.jpg"
        image_source5 = "https://live.staticflickr.com/8053/8417232675_06048bd47e_c.jpg"
        image_source6 = "https://i.pinimg.com/originals/a6/b8/7e/a6b87e757075eda9b43a0212228becf7.jpg"
        image_source7 = "https://cakesburg.co.uk/cdn/shop/products/Painting_relaxing_cake_10_800x.jpg?v=1535231450"
        image_source8 = "https://www.cravebyleena.com/cdn/shop/products/Artlove.png?v=1701592410"
        image_source9 = "https://pic.warmoven.in/catalog/product/cache/4e14bcb566d25893ae7201d4dbdc22fd/image/1340483e/painter-cake.png"
        image_source10 = "https://i.pinimg.com/originals/71/03/8d/71038dd5635c97305bceeb48486f1156.jpg"
        image_source11 = "https://m.media-amazon.com/images/I/814fqSef8rL.jpg"
        image_source12 = "https://thememyparty.in/cdn/shop/products/CakeTopper_4c19df2f-b729-4951-876b-d85fca3c8dc6_800x.jpg?v=1666934444"
        return template('dynamic',text='Baby Shower', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)

    elif _click=='bt4':
        image_source1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQw2DBC9YCJaP_RGGp25F74jl2ZhYACnSxLIw&usqp=CAU"
        image_source2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNg-N_H7csLw2kPiQemi-G-u9avLfXFO21fg&usqp=CAU"
        image_source3 = "https://www.yummycake.co.in/wp-content/uploads/2023/03/MAC-Makeup-Theme-Cake.jpg"
        image_source4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY6KhdUyaGPk_DlGkj--6MkYDLXRPRtzqM9A&usqp=CAU"
        image_source5 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjY6dzU-BK7IsUUyhK3mW2lMIKVEFOG7UBmQ&usqp=CAU"
        image_source6 = "https://www.adultcakes.in/wp-content/uploads/2018/06/makeup-kit-cake-1.jpg"
        image_source7 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTO_9JhQjjsbGQ5S93-fXNOXsKzConCtEWD7w&usqp=CAU"
        image_source8 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWsHzhazj7dvbo0LyMrKOk899yigfUV_hZLg&usqp=CAU"
        image_source9 = "https://www.kanpurgifts.com/admin/product_images/makeup%201.jpg"
        image_source10 = "https://www.cakeplaza.in/cdn/shop/products/Mac_x700.jpg?v=1611921003"
        image_source11 = "https://www.bakehoney.com/media/38948/conversions/33446_12-30-2022_16-38-30_name_000000000000Makeup-Theme-Cake-by-sweet-art-from-bakehoney-banner.jpg"
        image_source12 = "https://www.flavoursguru.com/image/catalog/catimg/primary/makeup-queen.jpg"

        return template('dynamic',text='Anniversary', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)
    elif _click=='bt5':
        image_source1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsJhkFInCLSk4NTan2U-9FgUHo_IYV2A2jEw&usqp=CAU"
        image_source2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQph-pfcepF1U216VhX487qWmg8_QMiMYw_dg&usqp=CAU"
        image_source3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8AerchnsrkH3cNKhZQcuA2hVXLlK3_BwJbg&usqp=CAU"
        image_source4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoqAoGvAwR8l5I4O60DT06lNllQl-Ygfvn4A&usqp=CAU"
        image_source5 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIy9ovTf98YHLTSqdEBRkxOTKC8YzZlpmzNg&usqp=CAU"
        image_source6 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUoHqXoZbNsVJbZdeO85EVFeoMCQIiXgVw4A&usqp=CAU"
        image_source7 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9XVM16-2CQM5tImhEd5D7G2crOXG0S24fAw&usqp=CAU"
        image_source8 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC2PXWiSfrMx5xYS3o2m0XJcrqZc3KOfwiPw&usqp=CAU"
        image_source9 = "https://www.thecaker.com/cdn/shop/products/School_theme_cake_1024x1024.jpg?v=1569680816"
        image_source10 = "https://www.chefrajanbakery.com/uploads_drop/1695220639Image-5514.jpg"
        image_source11 = "https://i.pinimg.com/originals/ae/50/a5/ae50a503874d756863875147759afa8a.jpg"
        image_source12 = "https://assets.winni.in/product/primary/2021/8/53421.jpeg?dpr=2&w=220"
        return template('dynamic',text='Anniversary', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)

    elif _click=='bt6':
        image_source1 = "https://assets.giftalove.com/resources/common/giftimages/productimage1/bodybuilder-themed-fondant-cake.jpg"
        image_source2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtiqDnVAsKrZWnamRlc8OSQev91Us5pSq-pQ&usqp=CAU"
        image_source3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrRBoWrcS54SCgY9SGZKJSlnXROCeWExHNTA&usqp=CAU"
        image_source4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNw9ZitASIY7EnarZo2rGOOz2c7mKLlux9iQ&usqp=CAU"
        image_source5 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu8WE_Z6_RTyB81dB1ScKgMhD-f2yY8FPaeQ&usqp=CAU"
        image_source6 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZGq1nwMSZPB6SL4KnyJjNiEISSmCLbnXUbw&usqp=CAU"
        image_source7 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_8kL6DkWYePoY9rO6h6PgOXJU5981wcoc7Q&usqp=CAU"
        image_source8 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjT521KhH9jYueNatB0kyl_gNqYXT7kF75-w&usqp=CAU"
        image_source9 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe8SIAG9AUD9b7KZ3K34dQpFAbkuQlt9wunA&usqp=CAU"
        image_source10 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDpaL0nn5-PWkV76Q2ulDEvp1sJ1BGKJ0YYyzTLOL-PbKpTO3ZaJLgRtUsngmrzYWQ5Js&usqp=CAU"
        image_source11 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy3UB2urYVZFcw3lEjtoZpZVjB0HAHhUkL3w&usqp=CAU"
        image_source12 = "https://i.pinimg.com/736x/d8/1a/67/d81a6770583f8af034c7e22f9a2157d3.jpg"
        return template('dynamic',text='Anniversary', source1=image_source1, source2=image_source2, source3=image_source3,
                        source4=image_source4, source5=image_source5,
                        source6=image_source6, source7=image_source7, source8=image_source8, source9=image_source9,
                        source10=image_source10, source11=image_source11, source12=image_source12)



@route('/action_page', method='post')
def logpage():


    emaildata=None
    email=request.forms.get('email')
    psw=request.forms.get('psw')
    log=request.forms.get('loginbutton')
    if(log=="login"):
        con = sqlite3.connect("arya_cake")
        print(email)
        print(psw)

@route('/action', method='post')
def logpage():
    mail=request.forms.get('signin')
    if (mail=="sign"):
        return template('signin')

@route('/signin',method='post')
def dataentry():
    data1= request.forms.get('email')
    data2 = request.forms.get('passw')

    data3 = request.forms.get('phone')
    data4 = request.forms.get('dob')

    birth_year = datetime.datetime.strptime(data4, "%Y-%m-%d").year
    current_year = datetime.datetime.now().year
    age = current_year - birth_year

    conf=request.forms.get('enter')
    d1=str(data3)
    d2=str(data2)
    d3=str(age)

    if conf=="done":
        check = None
        flg=1
        con = sqlite3.connect("arya_cakes_magic")
        query = "select email from customer"
        output=con.execute(query)
        con.commit()
        try:
            for row in output:
                if row=="data1":
                    flg==2
            if check==None and flg==1:
                query ="insert into customer(email,passwd,phone,dob,age) values ('" + data1 + "','" + d2 + "','" + d1 + "','" + data4 + "','" + d3 + "')"
                con.execute(query)
                con.commit()
                return products()

        except:
            return '<h1>Email Already Exist Enter Valid Email</h1>'
        con.close()
@route('/log_page',method='post')
def valid():
    try:
        global email
        data1= request.forms.get('email')
        d1=str(data1)
        email=d1
        d1=d1.lower()
        data2 = request.forms.get('psw')

        data2=str(data2)
        print(data1)
        print(data2)

        if data2=="kanad0207" and data1=="dandnaikmukta511@gmail.com":
            return orders()
        else:
            con = sqlite3.connect("arya_cakes_magic")
            mycur = con.cursor()
            query = "select passwd from customer where email='" + d1 + "';"
            mycur.execute(query)
            output=mycur.fetchone()
            output=str(output[0])
            print(output)

            con.commit()
            con.close()

            if output == data2:
                return plac()

            else:
                s='incorrect password'
                return template('logpage', message=s)

    except:
        return template('logpage', message="Something Went Wrong ")

@route('/conform',method='post')
def conform():
    try:
        global dic
        global i
        global customer
        global email
        global number
        global location
        global cake
        global date
        global weight
        global amount
        global image
        global common
        data1 = request.forms.get('name')
        data4 = request.forms.get('od')
        data5 = request.forms.get('address')
        data6 = request.forms.get('show')

        d1 = str(data1)
        d2 = str(data4)
        d3 = str(data5)
        customer = d1
        date = d2
        location = d3
        con = sqlite3.connect("arya_cakes_magic")
        mycur = con.cursor()
        query = "select phone from customer where email='" + email + "';"
        mycur.execute(query)
        output = mycur.fetchone()
        output = str(output[0])
        print(output)
        number=output
        con.commit()
        con.close()
        image1 = request.files.get('image')
        image = image1.file.read()


        if data6=='bt2':
            common=cake
            con = sqlite3.connect("arya_cakes_magic")
            query = "INSERT INTO `order` (customer, email, number, location, cake, orderdate, weight, amount,image) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)"
            values = (customer, email, number, location, cake, date, weight, amount,image)
            con.execute(query, values)
            con.commit()
            con.close()
            print(data6)
            i=i+1
            ch=None
            if image==None:
                ch ="none"
            else:
                ch="image"
            new_row = {'sr':i, 'customer':customer, 'email': email, 'number': number, 'location': location, 'cake': cake, 'date': date, 'weight': weight, 'amount': '1', 'image':ch}
            dic.append(new_row)
            image=None
            return thank()
        if data6 == 'bt1':
            con = sqlite3.connect("arya_cakes_magic")
            query = "INSERT INTO `order` (customer, email, number, location, cake, orderdate, weight, amount,image) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)"
            values = (customer, email, number, location, cake, date, weight, amount, image)
            con.execute(query, values)

            con.commit()
            con.close()
            print(data6)
            i = i + 1
            ch = None
            if image == None:
                ch = "none"
            else:
                ch = "image"
            new_row = {'sr': i, 'customer': customer, 'email': email, 'number': number, 'location': location,
                       'cake': cake, 'date': date, 'weight': weight, 'amount': '1', 'image': ch}
            dic.append(new_row)
            image = None
            return online()
    except:
        return buy()

@route('/ownertable',method='post')
def delete():

    data1 = request.forms.get('delete')
    if data1=="1":
        global dic,i
        i=0
        dic=[]
        return template('logpage', message='')
    if data1=="2":
        # List of phone numbers with country code (e.g., +1234567890)
        # phone_numbers = ['+918767963216', '+918975565456']
        current_time = datetime.datetime.now()
        # Extract the hour and minute separately
        current_hour = current_time.hour
        current_minute = current_time.minute
        today = datetime.datetime.now().date()

        # Calculate the day after tomorrow
        day_after_tomorrow = today + timedelta(days=2)

        # Get day and month separately
        day = day_after_tomorrow.day
        month = day_after_tomorrow.month

        print("Day after tomorrow's day:", day)
        print("Day after tomorrow's month:", month)
        if day > 0 and day < 10:
            s = str(day)
            day = '0' + s
        if month > 0 and month < 10:
            m = str(month)
            month = "0" + m

        day = str(day)
        month = str(month)
        s = '____-' + month + '-' + day
        print(s)
        message = 'Happy Birthday'
        con = sqlite3.connect("arya_cakes_magic")
        mycur = con.cursor()
        query = "select phone from customer where dob like'" + s + "'"
        mycur.execute(query)
        output = mycur.fetchall()
        con.commit()
        con.close()
        phone_numbers = [i[0] for i in output]
        hour = current_hour
        minute = current_minute + 1

        # Loop through each phone number and send the message
        for phone in phone_numbers:
            p = str(phone)
            final = '+91' + p
            # kit.sendwhatmsg(final, message, hour, minute)
            # Get the current date and time
            current_time = datetime.datetime.now()
            # Extract the hour and minute separately
            current_hour = current_time.hour
            current_minute = current_time.minute
            minute = current_minute + 1
            time.sleep(30)
            close_button_x = 1900
            close_button_y = 25

            # pyautogui.moveTo(close_button_x, close_button_y)
            # pyautogui.click()

            # Add a delay between messages to avoid rate limits (optional)

            time.sleep(5)
        return '<h1>Notification Send Sucessfully</h1>'

@route('/thank',method='post')
def you():
    data1 = request.forms.get('thank')
    if data1=="you":
        return products()

@route('/firstpage',method='post')
def page():
    try:
        global email
        data1= request.forms.get('email')
        d1=str(data1)
        email=d1
        d1=d1.lower()
        data2 = request.forms.get('psw')
        data2=str(data2)
        print(data1)
        print(data2)


        if data2=="kanad0207" and data1=="dandnaikmukta511@gmail.com":

            return orders()
        else:
            con = sqlite3.connect("arya_cakes_magic")
            mycur = con.cursor()
            query = "select passwd from customer where email='" + d1 + "';"
            mycur.execute(query)
            output=mycur.fetchone()
            output=str(output[0])
            print(output)

            con.commit()
            con.close()
            if output == data2:
                return plac()

            else:
                s='incorrect password'
                return template('logpage', message=s)

    except:
        return template('logpage', message="Something Went Wrong ")
@route('/firstpage')
def page():
    return template('firstlogin')


@route('/table', method='post')
def table():
        global cake
        global weight

        global dic,i
        data6 = request.forms.get('status')

        if data6=='accept':
            con = sqlite3.connect("arya_cakes_magic")
            query = "INSERT INTO `accept` (customer, email, location, cake, orderdate, weight, amount) VALUES (?, ?, ?, ?, ?, ?, ?)"
            values = (customer, email, location, cake, date, weight, str(amount))
            con.execute(query, values)
            con.commit()
            dic.pop(0)
            con.close()
            return orders()
        if data6=='reject':
            con = sqlite3.connect("arya_cakes_magic")
            query = "INSERT INTO `reject` (customer, email, location, cake, orderdate, amount) VALUES (?, ?, ?, ?, ?, ?)"
            values = (customer, email, location, common, date, str(amount))
            con.execute(query, values)
            con.commit()
            dic.pop(0)
            return orders()



run(debug=True, reloader=True,host='0.0.0.0',port=8080)



