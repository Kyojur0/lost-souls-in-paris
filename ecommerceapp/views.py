from django.shortcuts import render
from ecommerceapp.models import Contact
from django.contrib import messages
from ecommerceapp.models import Product
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category','product_id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params= {'allProds':allProds}
    return render(request,"index.html",params)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['desc']
        phone_number = request.POST['pnumber']
        query = Contact(
            name=name, email=email, subject=subject, phone_number=phone_number
        )
        query.save()
        messages.info(request, 'We will get back at you soon :)')
        return render(request, 'contact.html')
    return render(request, 'contact.html')

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to continue')
        return render(request, 'login.html')
    
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(
            items_json=items_json, name=name, amount=amount, email=email, 
            address1=address1, address2=address2, city=city, state=state, 
            zip_code=zip_code, phone=phone
        )
        order.save()
        update = OrderUpdate(
            order_id=order.order_id, update_desc="The order has been placed"
        )
        update.save()
        messages.info(request, 'Your order has been placed')
        thank = True
        

    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')