from django.urls import path, include
from django.contrib.auth import views as auth_views


from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("closed", views.closedindex, name="closed"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path("register", views.register, name="register"),
    path("listing/<int:listing>", views.listing, name="listing"),
    path("bid", views.bid, name="bid"),
    path("comment", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addtowatchlist/<int:item_id>", views.add_to_watchlist, name="add_to"),
    path("removefrom/<int:item_id>", views.remove_from, name="remove"),
    path("categories", views.categories, name="categories"),
    path("winner", views.winner, name="winner"),
    path("addListing", views.addListing, name="add_listing"),
    path("user_listings", views.user_listings, name="user_listings"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
    path('checkout/', views.checkout, name="checkout"),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),

    
   path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="auctions/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="auctions/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="auctions/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="auctions/password_reset_done.html"),
         name="password_reset_complete"),
]
