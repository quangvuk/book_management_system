from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher
from  django.utils.html import format_html
from django.db.models import Q # used to make OR condition for query statement

# admin.site.register(Book)

# define BookAdmin
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','owner',)
    search_fields = ['title','description']
    # fields = ['image_tag', ]
    # readonly_fields = ['image_tag',]
    readonly_fields = []
    #override readonly_fields
    def get_readonly_fields(self, request, obj=None):
        current_readony_fields = super(BookAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            current_readony_fields = ['owner']
        return current_readony_fields

    #
    def get_queryset(self, request):
        ds = super(BookAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return  ds
        return  ds.filter(owner=request.user.id)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(BookAdmin, self).get_search_results(request, queryset, search_term)
        try:
            #condition = Q(title.startswith(search_term)) | Q(description.startswith(search_term))
            queryset = queryset.filter(Q(title__istartswith = search_term) | Q(description__istartswith = search_term))  #self.model.objects.filter(title__startswith(search_term))
        except:
            pass
        return queryset, use_distinct




# define AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender')

# define PublisherAdmin
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','contact')

# register the admin class
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.sites.AdminSite.site_header = "BOOK MANAGEMENT SYSTEM"
admin.sites.AdminSite.site_url = "/admin"
