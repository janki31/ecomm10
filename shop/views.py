from django.shortcuts import render
from .models import Product,Contact,Order
from math import ceil
def index(request):
    #products=Product.objects.all()
    #print("products:- ",products)
    #n=len(products)
    #print("No of products:- ",n)
    #nslide=ceil(n/4)
    #print("No of slides:- ",nslide)
    #params={'nslide':nslide,'range':range(1,nslide),'product':products}
    #allprods=[[products,range(1,nslide),nslide],[products,range(1,nslide),nslide]]
    allprods=[]
    catprods=Product.objects.values('category','product_id')
    categorys={item['category'] for item in catprods}
    for c in categorys:
        prods=Product.objects.filter(category=c)
        #print("products:- ", prods)
        n = len(prods)
        nslide = ceil(n / 4)
        allprods.append([prods,range(1,nslide),nslide])
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)

def basic(request):
    return render(request,'shop/basic.html')
def contactus(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('cemail','')
        mobileno=request.POST.get('mobno','')
        feedback=request.POST.get('feedback','')
        contact=Contact(name=name,email=email,mobileno=mobileno,feedback=feedback)
        contact.save()
        #print(name," ",email," ",mobileno," ",feedback)
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def product(request,pid):
    pro=Product.objects.filter(product_id=pid)
    return render(request,'shop/products.html',{'pro':pro[0]})

def order(request):
    flag=False
    if request.method=='POST':
        itemjson=request.POST.get('cartitems','')
        fname=request.POST.get('firstName','')
        lname=request.POST.get('lastName','')
        email=request.POST.get('email','')
        address1=request.POST.get('address','')+ request.POST.get('address2','')
        mobileno=request.POST.get('mobno','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zip','')
        total=request.POST.get('total','')
        #print("total:- ",total)
        order=Order(itemjson=itemjson,fname=fname,lname=lname,email=email,address1=address1,
                    mobileno=mobileno,state=state,zipcode=zipcode,total=total)
        order.save()
        flag=True
        return render(request, 'shop/order.html',{'flag':flag})
    return render(request,'shop/order.html')

def searchmatch(search_text,item):
    if search_text.lower() in item.product_name.lower() or \
            search_text.lower() in item.category.lower() or \
            search_text.lower() in item.product_desc.lower():
        return True
    else:
        return False

def search(request):
    search_text=request.GET.get('search','')
    #print("search text:- ",search_text)
    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    categorys = {item['category'] for item in catprods}

    for c in categorys:
        prods=Product.objects.filter(category=c)
        sprods=[item for item in prods if searchmatch(search_text,item)]
        n = len(sprods)
        nslide = ceil(n / 4)
        if n!=0:
            allprods.append([sprods, range(1, nslide), nslide])
        params = {'allprods': allprods,'msg':""}
        if(len(allprods)==0):
            params={'msg':'please entern proper product name'}
    return render(request,'shop/search.html',params)
