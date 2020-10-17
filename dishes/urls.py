from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import (
    CheckoutView,
    ItemDetailView,
    contact,
    about,
    menu,
    faq,
    HomeView,
    add_to_cart,
    remove_from_cart,
    CategoryListView,
    OrderSummaryView,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    search
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('category/<category>', CategoryListView.as_view(), name='category-list'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('results/', search, name="search"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
