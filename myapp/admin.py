from django.contrib import admin
from .models import Product, Category,Supplier, SupplierDetail, HomePage, Commande
from decimal import Decimal
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('image_tag','name','price','supplier','quantity','stock_status','categories_list','short_description','formatted_created_at')
    search_fields=('name','description')
    list_filter=('quantity','price','created_at')
    ordering=('-name',)
    fields=('name','price','supplier','quantity','categories','description','image','image_tag','created_at')
    readonly_fields=('created_at','image_tag')
    list_per_page=10
    list_editable=('quantity','price')
    date_hierarchy='created_at'

    actions=['set_price_to_zero','duplicate_product','apply_discount']

    def formatted_created_at(self,obj):
        return obj.created_at.strftime('%d-%m-%Y %H:%M:%S')
    formatted_created_at.short_description='Created At'

    def short_description(self,obj):
        return obj.description[:20]+'...'
    short_description.short_description='Description'

    def set_price_to_zero(self,request,queryset):
        queryset.update(price=0)
        self.message_user(request,'Le prix des produits sélectionnés a été mis à 0')
    set_price_to_zero.short_description='Mettre le prix à 0'

    def duplicate_product(self,request,queryset):
        for product in queryset:
            product.pk=None
            product.save()
        self.message_user(request,'Les produits sélectionnés ont été dupliqués')
    duplicate_product.short_description='Dupliquer les produits'

    def apply_discount(self,request,queryset):
        discount_percentage = Decimal("0.9")  # Utiliser Decimal
        for product in queryset:
            if product.price:  # Vérifier que price est défini
                new_price = Decimal(product.price) * discount_percentage 
                product.price = new_price # Appliquer la remise
                product.save() 
        self.message_user(request, "La remise a été appliquée avec succès.")
    apply_discount.short_description = "Appliquer une remise de 10 pourcent"

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius:5px;" />'.format(obj.image.url))
        return "Pas d'image"

    image_tag.short_description = 'Aperçu'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','products_count')
    search_fields=('name',)
    list_per_page=10
    fields=('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ('name', 'phone')
    list_display = ('name', 'phone')
    search_fields = ['name'] 

@admin.register(SupplierDetail)  # Utiliser le nouveau nom ici
class SupplierDetailAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'address', 'contact_email', 'website', 'contact_person',)
    search_fields = ('contact_person',)
    list_filter = ('supplier',)
    fields = ('supplier', 'address', 'contact_email', 'website', 'contact_person', 'supplier_type', 
               'country', 'payment_terms', 'bank_account', 'region_served')
    list_per_page = 10

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'logo_tag','logo','welcome_titre', 'formatted_welcome_message', 'action1_message', 'action1_lien', 'action2_message', 'action2_lien', 'formatted_contact_message', 'formatted_about_message', 'formatted_footer_message', 'footer_bouton_message')
    fields = ('logo',  'site_name', 'welcome_titre', 'welcome_message', 'action1_message', 'action1_lien', 'action2_message', 'action2_lien', 'contact_message', 'about_message', 'footer_message', 'footer_bouton_message') 
    
    def logo_tag(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100px" style="border-radius:5px;" />'.format(obj.logo.url))
        return "Pas d'image"
    logo_tag.short_description = 'Logo'

    def formatted_welcome_message(self, obj):
        return format_html(obj.welcome_message)
    formatted_welcome_message.short_description = 'Message de bienvenue'

    def formatted_contact_message(self, obj):
        return format_html(obj.contact_message)
    formatted_contact_message.short_description = 'Message de contact'

    def formatted_about_message(self, obj):
        return format_html(obj.about_message)
    formatted_about_message.short_description = 'Message à propos'

    def formatted_footer_message(self, obj):
        return format_html(obj.footer_message)
    formatted_footer_message.short_description = 'Message du pied de page'

    def has_add_permission(self, request):
        # Empêcher l'ajout d'un nouvel objet si un existe déjà
        if HomePage.objects.exists():
            return False
        return True
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity','total_commande','customer_name', 'status_colored','customer_email', 'customer_phone','created_at', 'is_delivered','payment',)
    search_fields = ('customer_name', 'customer_email', 'customer_phone', 'customer_address')
    list_editable = ('is_delivered',)  
    list_filter = ('customer_name', 'payment')
    fields = ('product', 'quantity', 'customer_name', 'customer_email', 'customer_phone', 'customer_address', 'payment',)  # Ajouter le graphique ici
    list_per_page = 5

    def status_colored(self, obj):
        """Affiche le statut avec une couleur : vert si livré, rouge sinon"""
        color = "green" if obj.is_delivered else "red"
        status = "Livrée" if obj.is_delivered else "En attente"
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>', color, status)
 
    status_colored.short_description = 'Statut'

    def total_commande(self, obj):
        """Calcule le total de la commande"""
        return obj.quantity * obj.product.price if obj.product and obj.product.price else 0
 
    total_commande.short_description = 'Total (€)'  # Changer l'affichage du titre






