from django.shortcuts import render
from .models import Farmer, Buyer, Contract
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')


# ================= FARMER =================

def farmer(request):
    return render(request, 'farmer.html')


def farmer_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        village = request.POST['village']
        crop = request.POST['crop']
        password = request.POST['password']

        Farmer.objects.create(
            name=name,
            mobile=mobile,
            village=village,
            crop=crop,
            password=password
        )

        return render(request, 'farmer_register.html', {
            'success': 'Farmer registered successfully!'
        })

    return render(request, 'farmer_register.html')


def farmer_login(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['password']

        farmer = Farmer.objects.filter(
            mobile=mobile,
            password=password
        ).first()

        if farmer:

            # Logged-in farmer ID save
            request.session['farmer_id'] = farmer.id

            contracts = Contract.objects.filter(
                farmer=farmer
            )

            return render(request, 'farmer_dashboard.html', {
                'farmer': farmer,
                'contracts': contracts
            })

        else:
            return render(request, 'farmer_login.html', {
                'error': 'Invalid mobile or password!'
            })

    return render(request, 'farmer_login.html')


def farmer_contracts(request):

    farmer_id = request.session.get('farmer_id')

    if farmer_id:

        farmer = Farmer.objects.get(id=farmer_id)

        contracts = Contract.objects.filter(
            farmer=farmer
        )

        return render(request, 'farmer_contracts.html', {
            'farmer': farmer,
            'contracts': contracts
        })

    return render(request, 'farmer_login.html', {
        'error': 'Please login first!'
    })
def farmer_logout(request):

    request.session.flush()

    return render(request, 'farmer_login.html', {
        'success': 'You have been logged out successfully!'
    })

# ================= FARMER EDIT PROFILE =================

def farmer_edit_profile(request):
    farmer_id = request.session.get('farmer_id')

    if not farmer_id:
        return render(request, 'farmer_login.html', {
            'error': 'Please login first!'
        })

    farmer = get_object_or_404(Farmer, id=farmer_id)

    if request.method == 'POST':
        farmer.name = request.POST.get('name', '').strip()
        farmer.mobile = request.POST.get('mobile', '').strip()
        farmer.village = request.POST.get('village', '').strip()
        farmer.crop = request.POST.get('crop', '').strip()
        farmer.save()

        return render(request, 'farmer_profile.html', {
            'farmer': farmer,
            'success': 'Profile updated successfully!'
        })

    return render(request, 'farmer_edit_profile.html', {
        'farmer': farmer
    })

# ================= BUYER =================

def buyer(request):
    return render(request, 'buyer.html')


def buyer_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        company = request.POST['company']
        location = request.POST['location']
        password = request.POST['password']

        Buyer.objects.create(
            name=name,
            mobile=mobile,
            company=company,
            location=location,
            password=password
        )

        return render(request, 'buyer_register.html', {
            'success': 'Buyer registered successfully!'
        })

    return render(request, 'buyer_register.html')



def buyer_login(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['password']

        buyer = Buyer.objects.filter(
            mobile=mobile,
            password=password
        ).first()

        if buyer:
            request.session['buyer_id'] = buyer.id

            return redirect('/buyer/dashboard/')
         

        else:
            return render(request, 'buyer_login.html', {
                'error': 'Invalid mobile or password!'
            })

    return render(request, 'buyer_login.html')

def buyer_profile(request):
    buyer_id = request.session.get('buyer_id')

    if buyer_id:
        buyer = Buyer.objects.get(id=buyer_id)
        return render(request, 'buyer_profile.html', {
            'buyer': buyer
        })

    return render(request, 'buyer_login.html', {
        'error': 'Please login first!'
    })


def buyer_contracts(request):
    buyer_id = request.session.get('buyer_id')

    if buyer_id:
        buyer = Buyer.objects.get(id=buyer_id)
        contracts = Contract.objects.filter(buyer=buyer)

        return render(request, 'buyer_contracts.html', {
            'buyer': buyer,
            'contracts': contracts
        })

    return render(request, 'buyer_login.html', {
        'error': 'Please login first!'
    })


def buyer_available_farmers(request):
    buyer_id = request.session.get('buyer_id')

    if buyer_id:
        buyer = Buyer.objects.get(id=buyer_id)
        farmers = Farmer.objects.all()

        return render(request, 'buyer_available_farmers.html', {
            'buyer': buyer,
            'farmers': farmers
        })

    return render(request, 'buyer_login.html', {
        'error': 'Please login first!'
    })


def buyer_dashboard(request):
    buyer_id = request.session.get('buyer_id')

    if not buyer_id:
        return redirect('/buyer/login/')

    buyer = Buyer.objects.get(id=buyer_id)

    return render(request, 'buyer_dashboard.html', {
        'buyer': buyer
    })
# ================= BUYER EDIT PROFILE =================

def buyer_edit_profile(request):
    buyer_id = request.session.get('buyer_id')

    if not buyer_id:
        return render(request, 'buyer_login.html', {
            'error': 'Please login first!'
        })

    buyer = get_object_or_404(Buyer, id=buyer_id)

    if request.method == 'POST':
        buyer.name = request.POST.get('name', '').strip()
        buyer.mobile = request.POST.get('mobile', '').strip()
        buyer.company = request.POST.get('company', '').strip()
        buyer.location = request.POST.get('location', '').strip()
        buyer.save()

        return render(request, 'buyer_profile.html', {
            'buyer': buyer,
            'success': 'Profile updated successfully!'
        })

    return render(request, 'buyer_edit_profile.html', {
        'buyer': buyer
    })


# ================= CONTRACT =================

def contract(request):

    farmers = Farmer.objects.all()
    buyers = Buyer.objects.all()
    contracts = Contract.objects.all()

    if request.method == 'POST':

        farmer_id = request.POST['farmer']
        buyer_id = request.POST['buyer']
        crop = request.POST['crop']
        quantity = request.POST['quantity']
        price = request.POST['price']
        contract_date = request.POST['contract_date']

        Contract.objects.create(
            farmer_id=farmer_id,
            buyer_id=buyer_id,
            crop=crop,
            quantity=quantity,
            price=price,
            contract_date=contract_date
        )

        contracts = Contract.objects.all()

        return render(request, 'contract.html', {
            'farmers': farmers,
            'buyers': buyers,
            'contracts': contracts,
            'success': 'Contract created successfully!'
        })

    return render(request, 'contract.html', {
        'farmers': farmers,
        'buyers': buyers,
        'contracts': contracts
    })
def farmer_profile(request):

    farmer_id = request.session.get('farmer_id')

    if farmer_id:
        farmer = Farmer.objects.get(id=farmer_id)

        return render(request, 'farmer_profile.html', {
            'farmer': farmer
        })

    return render(request, 'farmer_login.html', {
        'error': 'Please login first!'
    })

# ================= FARMER CROP =================

def farmer_crop(request):

    farmer_id = request.session.get('farmer_id')

    if farmer_id:
        farmer = Farmer.objects.get(id=farmer_id)

        return render(request, 'farmer_crop.html', {
            'farmer': farmer
        })

    return render(request, 'farmer_login.html', {
        'error': 'Please login first!'
    })
# ================= DELIVERY STATUS =================

def farmer_delivery(request):

    farmer_id = request.session.get('farmer_id')

    if farmer_id:
        farmer = Farmer.objects.get(id=farmer_id)

        contracts = Contract.objects.filter(
            farmer=farmer
        )

        return render(request, 'farmer_delivery.html', {
            'farmer': farmer,
            'contracts': contracts
        })

    return render(request, 'farmer_login.html', {
        'error': 'Please login first!'
    })

# ================= ADMIN LOGIN =================

from django.contrib.auth import authenticate, login

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin-dashboard/')

        return render(request, 'admin_login.html', {
            'error': 'Invalid username or password!'
        })

    return render(request, 'admin_login.html')

@user_passes_test(lambda user: user.is_authenticated and user.is_staff, login_url='/admin-login/')
def admin_dashboard(request):

    farmers = Farmer.objects.all()
    buyers = Buyer.objects.all()
    contracts = Contract.objects.all()

    return render(request, 'admin_dashboard.html', {
        'farmers': farmers,
        'buyers': buyers,
        'contracts': contracts,
    })
# ================= ADMIN LOGOUT =================

def admin_logout(request):
    logout(request)
    return redirect('/admin-login/')
#_==================== Update status==============================
@user_passes_test(lambda user: user.is_authenticated and user.is_staff, login_url='/admin-login/')

def update_delivery_status(request, contract_id):
    if request.method == 'POST':
        contract = get_object_or_404(Contract, id=contract_id)

        status = request.POST.get('delivery_status')

        if status in ['Pending', 'In Progress', 'Delivered']:
            contract.delivery_status = status
            contract.save()

    return redirect('/admin-dashboard/')

#=====================Payment Status=====================
def farmer_payment(request):
    farmer_id = request.session.get('farmer_id')

    if farmer_id:
        farmer = Farmer.objects.get(id=farmer_id)
        contracts = Contract.objects.filter(farmer=farmer)

        return render(request, 'farmer_payment.html', {
            'farmer': farmer,
            'contracts': contracts
        })

    return render(request, 'farmer_login.html', {
        'error': 'Please login first!'
    })

    # ================= PAYMENT STATUS UPDATE =================
@user_passes_test(lambda user: user.is_authenticated and user.is_staff, login_url='/admin-login/')
def update_payment_status(request, contract_id):
    if request.method == 'POST':
        contract = get_object_or_404(Contract, id=contract_id)

        status = request.POST.get('payment_status')

        if status in ['Pending', 'Paid']:
            contract.payment_status = status
            contract.save()

    return redirect('/admin-dashboard/')

def farmer_dashboard(request):
    farmer_id = request.session.get('farmer_id')

    if not farmer_id:
        return redirect('/farmer/login/')

    farmer = get_object_or_404(Farmer, id=farmer_id)

    return render(request, 'farmer_dashboard.html', {
        'farmer': farmer
    })

def buyer_dashboard(request):
    buyer_id = request.session.get('buyer_id')

    if not buyer_id:
        return redirect('/buyer/login/')

    buyer = Buyer.objects.get(id=buyer_id)

    return render(request, 'buyer_dashboard.html', {
        'buyer': buyer
    })


# Buyer Logout

def buyer_logout(request):
    request.session.flush()
    return render(request, 'buyer_login.html', {
        'success': 'Logout successful! You have been logged out.'
    })