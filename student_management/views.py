from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
import pyrebase
from .models import Image

config = {"apiKey": "AIzaSyDsCFgv4NA_HTvYyxzw-VsBRM7P9hU58Go",
          "authDomain": "schoolprojectdb-b9bf7.firebaseapp.com",
          "databaseURL": "https://schoolprojectdb-b9bf7-default-rtdb.firebaseio.com",
          "projectId": "schoolprojectdb-b9bf7",
          "storageBucket": "schoolprojectdb-b9bf7.appspot.com",
          "messagingSenderId": "244932315635",
          "appId": "1:244932315635:web:d62d9ddd75a64fc8c16a86",
          "measurementId": "G-79N9CLY19V"
          }
firebase = pyrebase.initialize_app(config)


def home(request):
    return render(request, 'home.html')


def teacher(request):
    db = firebase.database()
    storage = firebase.storage()
    auth = firebase.auth()
    if request.method == 'POST':
        image = Image()
        name = request.POST.get('name', 'none')
        des = request.POST.get('des', 'none')
        key = db.generate_key()
        db.child("teacher").child(key).set({'key': key, 'name': name, 'des': des})

        if len(request.FILES) != 0:
            image.img = request.FILES['img']
            image.key = key
            image.save()
            storage.child("teacher").child(key).put(image.img)
            user = auth.sign_in_anonymous()
            imgUrl = storage.child("teacher/" + key).get_url(user['refreshToken'])
            db.child("teacher").child(key).child("url").set(imgUrl)
        return HttpResponseRedirect('/teacher')
    else:
        datas = db.child("teacher").get()
        dat = list(dict())
        if datas.val() is not None:
            for d in datas.each():
                val = ''
                lis = dict()
                for i, j in reversed(d.val().items()):
                    if i == 'key':
                        val = j
                    elif i == 'url':
                        lis['0'] = j
                    elif i == 'name':
                        lis['1'] = j
                    else:
                        lis['2'] = j
                lis['3'] = val
                dat.append(lis)
            return render(request, 'teacher.html', {'data': dat, 'null': 1})
        else:
            return render(request, 'teacher.html', {'null': 0})


def deleteData(request, key):
    db = firebase.database()
    storage = firebase.storage()
    auth = firebase.auth()
    if request.method == 'POST':
        page = request.POST.get('page', 'none')
        db.child(page).child(key).remove()
        user = auth.sign_in_anonymous()
        try:
            storage.delete(page + "/" + key, user["idToken"])
        except:
            print("An exception occurred")
        Image.objects.filter(key=key).delete()
        return HttpResponseRedirect('/' + page)


def updateData(request, key):
    db = firebase.database()
    storage = firebase.storage()
    auth = firebase.auth()
    url = ''
    try:
        im = Image.objects.filter(key=key)
        for i in im:
            url = i.img.url
    except:
        print("An exception occurred")

    if request.method == 'GET':
        page = request.GET.get('page', 'none')
        ch = 0
        if page == "teacher":
            ch = 1
        name = db.child(page).child(key).child("name").get().val()
        des = db.child(page).child(key).child("des").get().val()
        return render(request, 'updateData.html', {'name': name, 'des': des, 'url': url, 'key': key, 'ch':ch, 'page':page})
    else:
        page = request.POST.get('page', 'none')
        name = db.child(page).child(key).child("name").get().val()
        des = ""
        if page == "teacher":
            des = db.child(page).child(key).child("des").get().val()
        nameR = request.POST.get('name', 'none')
        desR = request.POST.get('des', 'none')
        urlR = 'none'
        if len(request.FILES) != 0:
            urlR = request.FILES['url']
        url1R = request.POST.get('url1', 'none')

        if name != nameR:
            db.child(page).child(key).update({"name": nameR})
        if page == "teacher" and des != desR:
            db.child(page).child(key).update({"des": desR})
        if urlR != 'none':
            ll = str(urlR)
            if ('/media/images/' + ll) != url:
                try:
                    cimg = Image.objects.get(key=key)
                    cimg.img = urlR
                    cimg.save()
                    user = auth.sign_in_anonymous()
                    try:
                        storage.delete(page+"/" + key, user["idToken"])
                    except:
                        print("An exception occurred")
                    storage.child(page).child(key).put(cimg.img)
                    imgUrl = storage.child(page+"/" + key).get_url(user['refreshToken'])
                    db.child(page).child(key).child("url").set(imgUrl)
                except:
                    image = Image()
                    image.img = request.FILES['url']
                    image.key = key
                    image.save()
                    user = auth.sign_in_anonymous()
                    storage.child(page).child(key).put(image.img)
                    imgUrl = storage.child(page+"/" + key).get_url(user['refreshToken'])
                    db.child(page).child(key).child("url").set(imgUrl)
        else:
            ll = str(url1R)
            if ('/media/images/' + ll) != url:
                try:
                    cimg = Image.objects.get(key=key)
                    cimg.img = url1R
                    cimg.save()
                    user = auth.sign_in_anonymous()
                    try:
                        storage.delete(page+"/" + key, user["idToken"])
                    except:
                        print("An exception occurred")
                    storage.child(page).child(key).put(cimg.img)
                    imgUrl = storage.child(page+"/" + key).get_url(user['refreshToken'])
                    db.child(page).child(key).child("url").set(imgUrl)
                except:
                    print("An exception occurred")
        return HttpResponseRedirect('/'+page)


def mentor(request):
    db = firebase.database()
    storage = firebase.storage()
    auth = firebase.auth()
    if request.method == 'POST':
        image = Image()
        name = request.POST.get('name', 'none')
        key = db.generate_key()
        db.child("mentor").child(key).set({'key': key, 'name': name})
        if len(request.FILES) != 0:
            image.img = request.FILES['img']
            image.key = key
            image.save()
            storage.child("mentor").child(key).put(image.img)
            user = auth.sign_in_anonymous()
            imgUrl = storage.child("mentor/" + key).get_url(user['refreshToken'])
            db.child("mentor").child(key).child("url").set(imgUrl)
        return HttpResponseRedirect('/mentor')
    else:
        datas = db.child("mentor").get()
        if datas.val() is not None:
            return render(request, 'mentor.html', {'data': datas, 'null': 1})
        else:
            return render(request, 'mentor.html')
