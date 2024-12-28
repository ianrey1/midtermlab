# customers/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm

# CreateView - Add a new customer
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer-list')  # Redirect to customer list after creation

# ListView - Display all customers
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

# DetailView - View details of a specific customer
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

# UpdateView - Edit an existing customer
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer-list')

# DeleteView - Delete a customer
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')
