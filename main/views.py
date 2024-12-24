from django.shortcuts import render, redirect, get_object_or_404
from .models import Bouquets, Category, Orders, OrderItem
from .forms import OrdersForm


def about(request):
    return render(request, 'main/about.html')

def bouquets(request):
    bouquets = Bouquets.objects.all()
    return render(request, 'main/bouquets.html', {'bouquets': bouquets})

def delivery(request):
    return render(request, 'main/delivery.html')

def order(request):
    error = ''
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            order = form.save()
            for bouquet_id, quantity in request.session.get('order', {}).items():
                bouquet = get_object_or_404(Bouquets, id=bouquet_id)
                OrderItem.objects.create(order=order, bouquet=bouquet, quantity=quantity)
            request.session['order'] = {}
            return redirect('order-success')
        else:
            error = 'Форма была не верной'

    form = OrdersForm()
    order_bouquets = []
    total_price = 0
    if 'order' in request.session:
        for bouquet_id, quantity in request.session['order'].items():
            bouquet = get_object_or_404(Bouquets, id=bouquet_id)
            bouquet.quantity = quantity
            order_bouquets.append(bouquet)
            total_price += bouquet.price * quantity

    return render(request, 'main/order.html', {
        'form': form,
        'error': error,
        'order_bouquets': order_bouquets,
        'total_price': total_price,
    })

def orderSuccess(request):
    return render(request, 'main/order-success.html')


def bouquets_view(request):

    min_price = Bouquets.objects.order_by('price').first().price if Bouquets.objects.exists() else 0
    max_price = Bouquets.objects.order_by('-price').first().price if Bouquets.objects.exists() else 10000

    price_min = int(request.GET.get('price_min', min_price))
    price_max = int(request.GET.get('price_max', max_price))
    selected_categories = request.GET.getlist('category')

    bouquets = Bouquets.objects.filter(price__gte=price_min, price__lte=price_max)

    if selected_categories:
        for category in selected_categories:
            bouquets = bouquets.filter(categories__name=category)
    bouquets = bouquets.order_by('price')

    categories = Category.objects.all()
    
    return render(request, 'main/bouquets.html', {
        'bouquets': bouquets.distinct(),
        'categories': categories,
        'min_price': min_price,
        'max_price': max_price,
        'selected_categories': selected_categories,
    })

def add_to_order(request, bouquet_id):
    if 'order' not in request.session:
        request.session['order'] = {}
    order = request.session['order']

    bouquet_id = str(bouquet_id)
    if bouquet_id in order:
        order[bouquet_id] += 1
    else:
        order[bouquet_id] = 1

    request.session.modified = True
    return redirect('bouquets')

def remove_from_order(request, bouquet_id):
    if 'order' in request.session:
        bouquet_id = str(bouquet_id) 
        if bouquet_id in request.session['order']:
            del request.session['order'][bouquet_id]
            request.session.modified = True
    return redirect('order')

def update_order_quantity(request, bouquet_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if 'order' not in request.session:
            request.session['order'] = {}

        bouquet_id = str(bouquet_id)
        request.session['order'][bouquet_id] = quantity
        request.session.modified = True

    return redirect('order')

