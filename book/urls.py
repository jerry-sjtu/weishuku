from django.conf.urls import patterns, url
from book import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^booklist/$', views.book_list, name='booklist'),
    url(r'^library/$', views.library, name='library'),
    url(r'^library/page/(?P<page>[0-9]+)/$', views.library_page, name='library_page'),
    url(r'^borrowed/$', views.borrowed, name='borrowed'),
    url(r'^borrowed/page/(?P<page>[0-9]+)/$', views.library_borrowed, name='library_borrowed'),
    url(r'^apply/$', views.apply, name='apply'),
    url(r'^apply/page/(?P<page>[0-9]+)/$', views.libray_applied, name='libray_applied'),
    url(r'^history/$', views.history, name='history'),
    url(r'^history/page/(?P<page>[0-9]+)/$', views.history_page, name='history_page'),
    url(r'^addbook/$', views.add_book, name='addbook'),
    url(r'^(?P<id>\d+)/$', views.info_book, name='info_book'),
    url(r'^borrow/$', views.borrow_book, name='borrow_book'),
    url(r'^approve_borrow/(?P<bookid>\d+)/$', views.approve_borrow, name='approve_borrow'),
    url(r'^refuse_borrow/(?P<bookid>\d+)/$', views.refuse_borrow, name='refuse_borrow'),
    url(r'^return/(?P<id>\d+)/$', views.return_book, name='return_book'),
    url(r'^search_book/(?P<keyword>.*)/$', views.search_book, name='search_book'),
)
