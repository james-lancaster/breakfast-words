from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from books.models import Book


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {book.title} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {book.title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified book to the specified amount"""
    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {book.title} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {book.title} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        book = get_object_or_404(Book, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed {book.title} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
