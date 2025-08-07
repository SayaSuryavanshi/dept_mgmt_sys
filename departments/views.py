from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Department
from .forms import DepartmentForm
from django.contrib.auth import logout

def is_admin(user):
    return user.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(dept_name__icontains=query, status=True)
    else:
        departments = Department.objects.filter(status=True)
    return render(request, 'departments/dashboard.html', {'departments': departments})

@login_required
@user_passes_test(is_admin)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DepartmentForm()
    return render(request, 'departments/add_department.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/edit_department.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        # soft delete
        messages.warning(request, "This department is now inactive.")
        department.status = False
        department.save()
        return redirect('dashboard')
    return render(request, 'departments/confirm_delete.html', {'department': department})

def user_logout(request):
    logout(request)
    return redirect('login') 