from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Avg , Count
from django.shortcuts import render,redirect

def shop_list_view(request,id):

    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
    except:
        cart_list = None

    category = Category.objects.get(id = id)
    
    product = Product.objects.filter(sub_category__category_id = id ).annotate(
            rating_count=Count('ratings'),
            avg_rating=Avg('ratings__rating')
        )

    for products in product:
        if products.avg_rating is not None:
            products.avg_rating *= 20
        else:
            products.avg_rating = 0
    size = Size.objects.all()
    sub_cat_name,subcat_items,sub_cat_id = [],[],[]
    subcat = SubCategory.objects.filter(category_id = id)
    for i in subcat:
        product_count = product.filter(sub_category = i).count()
        subcat_items.append(product_count)
        sub_cat_name.append(i.name)
        sub_cat_id.append(i.id)
    subcat_data = zip(sub_cat_id,sub_cat_name,subcat_items)
    if request.GET.get("search"):
        product = product.filter(name__icontains = request.GET.get("search"))
    if request.GET.get("sort"):
        if request.GET.get("sort") == "1":
            product = product.filter().order_by("name")
        if request.GET.get("sort") == "2":
            product = product.filter().order_by("-name")
        if request.GET.get("sort") == "3":
            product = product.filter().order_by("price")
        if request.GET.get("sort") == "4":
            product = product.filter().order_by("-price")
    if request.GET.get("cat"):
        product = product.filter(sub_category_id = request.GET.get("cat"))
    if request.GET.get("size"):
        product = product.filter(sizes__id__in=request.GET.get("size"))
    if request.GET.get("price"):
        s_p = request.GET.get("price").split('-')[0]
        l_p = request.GET.get("price").split('-')[1]
        product = product.filter(price__range=(int(request.GET.get("price").split('-')[0]),int(request.GET.get("price").split('-')[1])))
        return render(request, 'products/shop-left-sidebar.html',{"products":product,"size":size,"subcat":subcat_data,
                                                                "id":id, "sort":str(request.GET.get("sort")) if request.GET.get("sort") else "",
                                                                "search":request.GET.get("search") if request.GET.get("search") else "",
                                                                "cat": request.GET.get("cat") if request.GET.get("cat") else "",
                                                                "s_p": s_p if s_p else "",
                                                                "l_p": l_p if l_p else 7000,"cart_list":cart_list,
                                                                "shop_data":shop_data
                                                                })
    print(product)
    return render(request, 'products/shop-left-sidebar.html',{"products":product,"size":size,"subcat":subcat_data,
                                                            "id":id, "sort":str(request.GET.get("sort")) if request.GET.get("sort") else "",
                                                            "search":request.GET.get("search") if request.GET.get("search") else "",
                                                            "cat": request.GET.get("cat") if request.GET.get("cat") else "",
                                                            "s_p": 0,
                                                            "l_p": 7000,
                                                            "wish_list":wish_list,"cart_list":cart_list,
                                                            "shop_data":shop_data
                                                            })

def shop_list(request,id):

    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
    except:
        cart_list = None

    if request.GET.get("cat1") == "true":
        product = Product.objects.filter(sub_category__category_id = id ).annotate(
                rating_count=Count('ratings'),
                avg_rating=Avg('ratings__rating')
            )
    else:
        product = Product.objects.filter(sub_category_id = id ).annotate(
            rating_count=Count('ratings'),
            avg_rating=Avg('ratings__rating')
        )
    

    for products in product:
        if products.avg_rating is not None:
            products.avg_rating *= 20
        else:
            products.avg_rating = 0
    size = Size.objects.all()
    sub_cat_name,subcat_items,sub_cat_id = [],[],[]
    subcat = SubCategory.objects.filter(category_id = id)
    for i in subcat:
        product_count = product.filter(sub_category = i).count()
        subcat_items.append(product_count)
        sub_cat_name.append(i.name)
        sub_cat_id.append(i.id)
    subcat_data = zip(sub_cat_id,sub_cat_name,subcat_items)
    if request.GET.get("search"):
        product = product.filter(name__icontains = request.GET.get("search"))
    if request.GET.get("sort"):
        if request.GET.get("sort") == "1":
            product = product.filter().order_by("name")
        if request.GET.get("sort") == "2":
            product = product.filter().order_by("-name")
        if request.GET.get("sort") == "3":
            product = product.filter().order_by("price")
        if request.GET.get("sort") == "4":
            product = product.filter().order_by("-price")
    if request.GET.get("cat"):
        product = product.filter(sub_category_id = request.GET.get("cat"))
    if request.GET.get("size"):
        product = product.filter(sizes__id__in=request.GET.get("size"))
    if request.GET.get("price"):
        s_p = request.GET.get("price").split('-')[0]
        l_p = request.GET.get("price").split('-')[1]
        product = product.filter(price__range=(int(request.GET.get("price").split('-')[0]),int(request.GET.get("price").split('-')[1])))
        return render(request, 'products/shop-left-sidebar.html',{"products":product,"size":size,"subcat":subcat_data,
                                                                "id":id, "sort":str(request.GET.get("sort")) if request.GET.get("sort") else "",
                                                                "search":request.GET.get("search") if request.GET.get("search") else "",
                                                                "cat": request.GET.get("cat") if request.GET.get("cat") else "",
                                                                "s_p": s_p if s_p else "",
                                                                "l_p": l_p if l_p else 7000,"cart_list":cart_list,
                                                                "shop_data":shop_data
                                                                })
    print(product)
    return render(request, 'products/shop-left-sidebar.html',{"products":product,"size":size,"subcat":subcat_data,
                                                            "id":id, "sort":str(request.GET.get("sort")) if request.GET.get("sort") else "",
                                                            "search":request.GET.get("search") if request.GET.get("search") else "",
                                                            "cat": request.GET.get("cat") if request.GET.get("cat") else "",
                                                            "s_p": 0,
                                                            "l_p": 7000,
                                                            "wish_list":wish_list,"cart_list":cart_list,
                                                            "shop_data":shop_data
                                                            })

def shop_product_detail(request,id):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
        wishlist_products = wish_list.filter(created_by=request.user).values_list('product', flat=True)
    except:
        wish_list = None
        wishlist_products = None

    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
    except:
        cart_list = None

    product = Product.objects.get(id = id )

    average_rate = Ratings.objects.filter(product=product)[0:3]
    rating_counts = Ratings.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']

    related_product = Product.objects.filter(sub_category = product.sub_category ).annotate(
        rating_count=Count('ratings'),
        avg_rating=Avg('ratings__rating')
    ).order_by('-id')[0:6]
    for product in related_product:
        if product.avg_rating is not None:
            product.avg_rating *= 20
        else:
            product.avg_rating = 0

    try:
        for product in related_product:
            average_rating = Ratings.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
            related_product.average_rating = average_rating * 20
            related_product.count = Ratings.objects.filter(product=product).count()
    except:
        related_product.average_rating = 0
        related_product.count = 0

    p_i = ProductImage.objects.filter(product_id = id).last()

    product_ids = Product.objects.get(id = id )
    try:
        ProdutHistory.objects.create(project = product_ids,created_by=request.user)
    except:
        pass
    return render(request, 'products/single-product.html', { "data":product,"related_product":related_product,"wish_list":wish_list,"p_i":p_i,"product_ids":product_ids,
               "average_rate":average_rate,"rating_counts":rating_counts,"wishlist_products":wishlist_products,"cart_list":cart_list,"shop_data":shop_data })

def cart_details(request):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    try:
        cart_total = 0
        grand_total = 0
        shipping_price = 100
        cart_list = CartItem.objects.filter(created_by = request.user)
        for i in cart_list:
            cart_total += i.total_price
        grand_total = cart_total + shipping_price
    except:
        cart_list = None
    if cart_list:
        return render(request, 'products/cart.html',{"wish_list":wish_list,"cart_list":cart_list,"grand_total":grand_total,
                                                    "shipping_price":shipping_price,"cart_total":cart_total,"shop_data":shop_data})
    else:
        return render(request, 'products/empty-cart.html',{"wish_list":wish_list})

def add_to_cart(request,id):
    
    product = Product.objects.get(id = id)
    if request.user.is_authenticated:
        # if request.method == "POST":
        product = Product.objects.get(id = id)
        if CartItem.objects.filter(product = product, created_by = request.user ):
            messages.success(request, 'This product already added to you cart')
            return redirect('products:shop_product_detail',product.id)

        if not request.POST.get("size"):
            messages.success(request, 'Please select size first')
            return redirect('products:shop_product_detail',product.id)

        if not request.POST.get("color"):
            messages.success(request, 'Please select color first')
            return redirect('products:shop_product_detail' , product.id )

        if product.discount:
            price = product.discount
        else:
            price = product.price
        try:
            cart = Cart.objects.get(created_by = request.user)
        except:
            cart = Cart.objects.create( created_by = request.user )
        
        cart_product = CartItem.objects.create(product = product, cart = cart , price = price, 
                                                size = request.POST.get("size"),
                                                color = request.POST.get("color"),
                                                total_price = int(request.POST.get("quantity")) * int(price),
                                                quantity = request.POST.get("quantity"),
                                                created_by = request.user
                                                )

        messages.success(request, 'Product added to cart successfully')
        return redirect('products:cart_details')
    else:
        messages.success(request, 'Please login first to proceed further!')
        return redirect('products:shop_product_detail' , product.id)

def clear_one_cart(request,id):
    cart = Cart.objects.get(id = id)
    if cart:
        cart.delete()
    messages.success(request, 'Product removed from your cart successfully')
    return redirect('products:cart_details')

def clear_cart(request):
    cart = Cart.objects.filter(created_by = request.user )
    if cart:
        cart.delete()
    messages.success(request, 'Product removed from your cart successfully')
    return redirect('frontend:index')

def wishlist_details(request):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    if request.user.is_authenticated:
        product = Product.objects.get(id = request.GET.get("id"))
        try:
            wish_list = Wishlist.objects.get(product = product , created_by = request.user)
            wish_list.delete()
            messages.success(request, 'Product removed from your wishlist')
        except:
            wish_list = Wishlist.objects.create(product = product , created_by = request.user)
            messages.success(request, 'Product added from your wishlist')
        return redirect('frontend:index')
    else:
        messages.success(request, 'PLease login first to add this item to you wishlist!')
        return redirect('frontend:index')
    return render(request, 'products/wishlist.html',{"shop_data":shop_data})

def user_wishlist(request):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
    except:
        cart_list = None
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    return render(request, 'products/wishlist.html',{"wish_list":wish_list,"cart_list":cart_list,"shop_data":shop_data})

def checkout(request):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        cart = Cart.objects.get(created_by = request.user)
        coupan = Coupans.objects.get(id = cart.run_time_coupan)
    except:
        coupan = None
        cart = None
    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
        grand_total = 0
        shipping_price = 100
        cart_list = CartItem.objects.filter(created_by = request.user)
        for i in cart_list:
            grand_total += i.total_price
        
        total = grand_total + shipping_price
        try:
            discounted_price = ( float(total) * float(coupan.percentage) ) / 100
        except:
            discounted_price = None
        try:
            discounted_t = float(total) - float(discounted_price)
        except:
            discounted_t = None
    except:
        cart_list = None
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    print(discounted_t,">>>>>>>>>>>>.",discounted_price)
    return render(request, 'products/checkout.html',{"wish_list":wish_list,"rating":rating,"cart_list":cart_list,"cart":cart,"discounted_price":discounted_price,
                                               "discounted_t":discounted_t, "total":total,"shipping_price":shipping_price,"shop_data":shop_data,"coupan":coupan})

def placeOrder(request):
    if request.method =="POST":
        cart_t = Cart.objects.get(created_by = request.user)
        cart = CartItem.objects.filter(created_by = request.user)
        order = Order.objects.create(first_name = request.POST.get("first_name"),
        last_name = request.POST.get("last_name"),
        email = request.POST.get("email"),
        phone = request.POST.get("phone"),
        address = request.POST.get("address") + " " + request.POST.get("address1")  ,
        state = request.POST.get("state"),
        city = request.POST.get("city"),
        zipcode = request.POST.get("zipcode"),
        message = request.POST.get("message"),
        created_by = request.user
        )
        try:
            print("OKKKKKKKKKKKKKKKKKKKKKKKKKKK")
            coupan = Coupans.objects.get(id = cart_t.run_time_coupan)
            cart_list = CartItem.objects.filter(created_by = request.user)
            grand_totals = 0
            for i in cart_list:
                grand_totals += i.total_price
        
            total = grand_totals + 100
            try:
                discounted_price = ( float(total) * float(coupan.percentage) ) / 100
            except:
                discounted_price = None
            try:
                discounted_t = float(total) - float(discounted_price)
            except:
                discounted_t = None
            print(total,"*****",discounted_price,"****",discounted_t)
            order.grand_total = float(discounted_t)
            order.discounted_price = float(discounted_price)
            order.coupan = coupan
            order.save()
        except:
            print("NOOOOOOOOOOOOOOOOO")

            grand_totals = 0
            cart_list = CartItem.objects.filter(created_by = request.user)
            for i in cart_list:
                grand_totals += i.total_price
            total = grand_totals + 100
            order.grand_total = total
            order.save()
            print(grand_totals,"*****")
        for i in cart:
            order_items = OrderItems.objects.create(
                                                    order = order,
                                                    product = i.product,
                                                    created_by = request.user,
                                                    quantity = i.quantity,
                                                    size = i.size,
                                                    color = i.color,
                                                    price = i.price,
                                                    total_price = i.total_price,

            )
            product = Product.objects.get(id = i.product.id)
            try:
                product.quantity = int(product.quantity) - int(i.quantity)
                product.save()
            except:
                product.quantity = 0
                product.save()
                
        
        cart.delete()
        cart_t.delete()
        messages.success(request, 'Your order is placed successfully')
        return redirect('frontend:index')

def rating(request,id):
    product = Product.objects.get(id = id)
    if request.method == "POST":
        rating = Ratings.objects.create(product = product , name = request.POST.get("name"),email=request.POST.get("name"),
                                        message = request.POST.get("message"),rating = request.POST.get("rating") )
        
        messages.success(request, 'Rating given successfully')
    return redirect('products:shop_product_detail' , product.id )

def update_cart(request):
    if request.method == "POST" and request.is_ajax():
        cart_id = request.POST.get("cart_id")
        newQuantity = request.POST.get("newQuantity")
        cart = CartItem.objects.get(id = int(cart_id))
        if cart:
            cart.quantity = int(request.POST.get("newQuantity"))
            cart.total_price = int(request.POST.get("newQuantity")) * int(cart.price)
            cart.save()
            response_data = {'message': 'Cart item updated successfully'}
            return JsonResponse(response_data, status=200)
        else:
            response_data = {'message': 'Cart item updated successfully'}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'message': 'Invalid request'}
        return JsonResponse(response_data, status=400)

def apply_promocode(request):
    if request.method == "POST" and request.is_ajax():
        promo = request.POST.get("promo")
        promocode = Coupans.objects.filter(name = promo).last()
        if promocode:
            response_data = {'message': 'found',"name":promocode.name,"percentage":promocode.percentage}
            cart = Cart.objects.get(created_by = request.user)
            cart.run_time_coupan = promocode.id
            cart.save()
            return JsonResponse(response_data, status=200)
        else:
            response_data = {'message': 'not found'}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'message': 'Invalid request'}
        return JsonResponse(response_data, status=400)