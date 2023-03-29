from django.shortcuts import *
# render,redirect
from django.views.generic import View
from .models import *

# Create your views here.
class Base(View):
    context = {}

class HomeView(Base):
    def get(self,request):
        self.context['categories'] = Category.objects.all()
        self.context['subcategories'] = SubCategory.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['ads'] = Ad.objects.all()
        self.context['brands'] = Brand.objects.all()
        self.context['hot_product'] = Product.objects.filter(labels = 'hot')
        self.context['new_product'] = Product.objects.filter(labels = 'new')
        self.context['reviews'] = Review.objects.all()

        return render(request,'index.html',self.context)

class CategoryView(Base):
    def get(self,request,slug):
        ids = Category.objects.get(slug = slug).id
        self.context['category_product'] = Product.objects.filter(category_id = ids)

        return render(request,'category.html',self.context)

class DetailView(Base):
    def get(self,request,slug):
        self.context['product_detail'] = Product.objects.filter(slug = slug)
        self.context['categories'] = Category.objects.all()
        self.context['brands'] = Brand.objects.all()
        all_brand = []
        for i in Brand.objects.all():
            ids = Brand.objects.get(name = i).id
            count = Product.objects.filter(brand = ids).count()
            all_brand.append({'product_count':count,'ids':ids})
            self.context['counts'] = all_brand

        return render(request,'product-detail.html',self.context)

class SearchView(Base):
    def get(self,request):
        query = request.GET.get('query')
        print(query)
        if not query:
#or if query == '':
            return redirect('/')
        self.context['search_product'] = Product.objects.filter(name__icontains = query)
        return render(request,'search.html',self.context)


from django.contrib.auth.models import User
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword == password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'The email is already taken')
                return redirect('/signup')

            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = f_name,
                    last_name = l_name,
                    password = password
                    )
                user.save()
                return redirect('/signup')
        else:
            messages.error(request,'Password does not match!')
            return redirect('/signup')

    return render(request,'signup.html')