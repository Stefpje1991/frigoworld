from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def item_list(request):
    items = Item.objects.filter(beschikbaar=True).order_by('naam')
    context = {
        'items': items
    }
    return render(request, 'items/item_list.html', context=context)


def filter_items(request):
    category = request.GET.get('category', 'Professioneel')  # Default waarde 'Professioneel'
    items = Item.objects.filter(categorie=category)  # Pas dit aan naar je veldnaam

    return render(request, 'items/item_filtered.html', {'items': items})


def item_overview(request):
    items = Item.objects.all().order_by('naam')
    return render(request, 'items/admin/item_overview.html', {'items': items})


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_overview')
    else:
        form = ItemForm()
    return render(request, 'items/admin/item_create.html', {'form': form})


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('item_overview')
    else:
        form = ItemForm(instance=item)
        id = pk

        context = {
            'form': form,
            'id': id
        }
    return render(request, 'items/admin/item_update.html', context=context)


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_overview')
    return render(request, 'items/admin/item_confirm_delete.html', {'item': item})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'items/item_detail.html', context=context)
