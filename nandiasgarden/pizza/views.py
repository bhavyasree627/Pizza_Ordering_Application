from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm

def home(request):
    return render(request,'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method=="POST":
        filled_form = PizzaForm(request.POST,request.FILES)
        if filled_form.is_valid():
            note = "Thanks for ordering %s, %s and %s pizza" %(filled_form.cleaned_data['size'],filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'])
            new_form=PizzaForm()
            return render(request,'pizza/order.html',{'pizzaform':new_form,'note':note,'multiple_form':multiple_form})
    else:
        form = PizzaForm()
        return render(request,'pizza/order.html',{'pizzaform': form,"multiple_form":multiple_form })
    
def pizzas(self):
    num_of_pizzas=2
    filled_multiple_pizza_form=MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        num_of_pizzas=filled_multiple_pizza_form.cleaned_data("number")
    PizzaForSet=formset_factory(PizzaForm,extra=num_of_pizzas)
    formset=PizzaForSet()
    if request.method == "POST":
        filled_formset=PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data('topping1'))
            note ="Pizzas have been ordered"
        else:
            note="Order was not placed, Please try again"
    return render(request,"pizza/pizzas.html",{'note':note,'formset':formset})